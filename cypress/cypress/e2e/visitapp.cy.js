describe("Login", () => {
  it("passes", () => {
    cy.visit("http://localhost:5000");
    cy.get(".btn.btn-info.btn-lg").click();

    cy.get(
      "body > section:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
    ).type("root");

    cy.get("#password").type("root");

    cy.get("button[class='btn btn-primary']").click();

    Cypress.on("uncaught:exception", (err, runnable) => {
      // returning false here prevents Cypress from
      // failing the test
      return false;
    });
  });
});
