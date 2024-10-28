const {sayHello} = require("./main.js")

describe("main.test.js ensure it is identifies", ()=>{
  it("should return true", ()=>{
    expect(true).toBe(true)
  })
})

it("ensure sayHello was imported properly", ()=>{
  expect(sayHello()).toBe("Hello")
})