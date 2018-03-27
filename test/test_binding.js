const CudaNapi = require("../lib/binding.js");
const assert = require("assert");

assert(CudaNapi, "The expected module is undefined");

function testBasic()
{
    const instance = new CudaNapi({
      "hash": "keccak-sha-256"
    });
    assert(instance.info, "The expected method is not defined");
    assert.strictEqual(instance.info(), "", "Unexpected value returned");
}

function testInvalidParams()
{
    const instance = new CudaNapi();
}

assert.doesNotThrow(testBasic, undefined, "testBasic threw an expection");
assert.throws(testInvalidParams, undefined, "testInvalidParams didn't throw");

console.log("Tests passed- everything looks OK!");