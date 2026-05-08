import { describe, test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync, readdirSync } from 'node:fs'
import { join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { Parser, Store, DataFactory } from 'n3'

const { namedNode } = DataFactory

const SHAPES_DIR = resolve(fileURLToPath(new URL('.', import.meta.url)), '../shapes')

const RDF_TYPE      = namedNode('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
const SH_NODE_SHAPE = namedNode('http://www.w3.org/ns/shacl#NodeShape')
const SH_NAME       = namedNode('http://www.w3.org/ns/shacl#name')
const DCT_CREATED   = namedNode('http://purl.org/dc/terms/created')
const VS_STATUS     = namedNode('http://www.w3.org/2003/06/sw-vocab-status/ns#term_status')

const EXPECTED_NS  = 'https://solidproject.org/shapes/'
const VALID_STATUS = new Set(['unstable', 'testing', 'stable', 'archaic'])

const files = readdirSync(SHAPES_DIR)
  .filter(f => f.endsWith('.ttl'))
  .map(f => ({ name: f, path: join(SHAPES_DIR, f) }))

// Parse once per file; cache result or error
const cache = new Map()
function parseFile(filePath) {
  if (cache.has(filePath)) return cache.get(filePath)
  const p = new Promise((res, rej) => {
    const quads = []
    new Parser().parse(readFileSync(filePath, 'utf-8'), (err, quad, prefixes) => {
      if (err) rej(err)
      else if (quad) quads.push(quad)
      else res({ store: new Store(quads), prefixes: prefixes ?? {} })
    })
  })
  cache.set(filePath, p)
  return p
}

describe('shapes/', () => {
  test('directory contains TTL files', () => {
    assert.ok(files.length > 0, 'No .ttl files found in shapes/')
  })

  for (const { name, path } of files) {
    describe(name, () => {

      test('valid Turtle syntax', async () => {
        await assert.doesNotReject(parseFile(path), `${name}: Turtle syntax error`)
      })

      test('NodeShapes have required metadata', async () => {
        const { store } = await parseFile(path)
        for (const shape of store.getSubjects(RDF_TYPE, SH_NODE_SHAPE, null)) {
          const id = shape.value

          assert.ok(
            store.getObjects(shape, SH_NAME, null).length > 0,
            `${id}: missing sh:name`
          )

          const created = store.getObjects(shape, DCT_CREATED, null)
          assert.ok(created.length > 0, `${id}: missing dct:created`)
          if (created.length > 0) {
            assert.match(
              created[0].value,
              /^\d{4}-\d{2}-\d{2}$/,
              `${id}: dct:created must be ISO 8601 date (YYYY-MM-DD), got "${created[0].value}"`
            )
          }

          const statuses = store.getObjects(shape, VS_STATUS, null)
          assert.ok(statuses.length > 0, `${id}: missing vs:term_status`)
          if (statuses.length > 0) {
            const s = statuses[0].value
            assert.ok(
              VALID_STATUS.has(s),
              `${id}: vs:term_status "${s}" must be one of ${[...VALID_STATUS].sort().join(', ')}`
            )
          }
        }
      })

      test('NodeShape URIs follow namespace and naming conventions', async () => {
        const { store } = await parseFile(path)
        for (const shape of store.getSubjects(RDF_TYPE, SH_NODE_SHAPE, null)) {
          if (shape.termType === 'BlankNode') continue
          const uri = shape.value

          assert.ok(
            uri.startsWith(EXPECTED_NS),
            `<${uri}>: must start with ${EXPECTED_NS}`
          )

          const local = uri.includes('#') ? uri.split('#').pop() : uri.split('/').pop()
          assert.ok(local.endsWith('Shape'), `<${uri}>: local name "${local}" must end with "Shape"`)
          assert.ok(
            local[0] === local[0].toUpperCase(),
            `<${uri}>: local name "${local}" must start with uppercase (PascalCase)`
          )
        }
      })

      test('namespace prefixes use lowercase and valid characters', async () => {
        const { prefixes } = await parseFile(path)
        for (const prefix of Object.keys(prefixes)) {
          if (!prefix) continue
          assert.match(
            prefix,
            /^[a-z][a-z0-9\-_]*$/,
            `${name}: prefix "${prefix}" must start with lowercase and contain only [a-z0-9-_]`
          )
        }
      })

    })
  }
})
