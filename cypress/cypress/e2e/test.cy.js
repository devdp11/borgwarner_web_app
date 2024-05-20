describe("test", () => {
  it("test", () => {
    //enter website
    cy.visit("http://localhost:5000");

    //fazer login
    cy.get(".btn.btn-info.btn-lg").click();
    cy.get(
      "body > section:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
    ).type("root");
    cy.get("#password").type("root");
    cy.get("button[class='btn btn-primary']").click();

    Cypress.on("uncaught:exception", (err, runnable) => {
      // returning false here prevents Cypress from
      // failing the test with cors
      return false;
    });

    //entrar quest
    cy.get(".nav-link.collapsed").click();
    cy.get(
      "body > div:nth-child(2) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > nav:nth-child(1) > a:nth-child(1)"
    ).click();

    //preencher quest
    cy.get(":nth-child(1) > .form-control").type("1234");
    cy.get("#pl").select("2");
    cy.wait(500);

    //segurança
    cy.get(
      ":nth-child(5) > tbody > tr > :nth-child(5) > .form-check > #flexCheckDefault"
    ).click();
    cy.get('[name="cestexto"]').type("Sou o mais seguro");

    //o-qualidade
    cy.get(
      ":nth-child(9) > tbody > tr > :nth-child(5) > .form-check > #flexCheckDefault"
    ).click();
    cy.get('[name="oqtexto"]').type("Los mejores que tien");

    //o-resultados
    cy.get(
      ":nth-child(13) > tbody > tr > :nth-child(5) > .form-check > #flexCheckDefault"
    ).click();

    //interpessoal
    cy.get(
      ":nth-child(18) > tbody > tr > :nth-child(5) > .form-check > #flexCheckDefault"
    ).click();

    //equipa
    cy.get(
      ":nth-child(23) > tbody > tr > :nth-child(5) > .form-check > #flexCheckDefault"
    ).click();

    //tecnicas-funcionais
    cy.get(
      ":nth-child(1) > tbody > tr > :nth-child(5) > .form-check > #flexCheckDefault"
    ).click();

    //pontualidade
    cy.get(
      ":nth-child(6) > tbody > tr > :nth-child(3) > .form-check > #flexCheckDefault"
    ).click();

    //assiduidade
    cy.get(
      ":nth-child(11) > tbody > tr > :nth-child(3) > .form-check > #flexCheckDefault"
    ).click();

    //a-global
    cy.get(":nth-child(6) > .form-check > #flexCheckDefault").click();

    //submit
    cy.get("#range").click();
    cy.wait(3000);

    //go back
    cy.get(".alert > :nth-child(1)").contains("Submetido com Sucesso");
    // Clique no botão após a submissão bem-sucedida
    cy.get(".nav-link").click();
  });
});
