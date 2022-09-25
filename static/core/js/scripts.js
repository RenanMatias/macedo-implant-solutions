$(document).ready(function() {
    let value = $("#menu").attr("id");

    $("#menu").click(function() {
        if (value === "menu") {
            $("#nav-close").show();
            $("#nav-open").hide();
            value = "close"
        } else {
            $("#nav-close").hide();
            $("#nav-open").show();
            value = "menu"
        }
    })

    var $clientCPF = $("#id_cpf");
    $clientCPF.mask('000.000.000-00', { reverse: true });
    var $clientCNPJ = $("#id_cnpj");
    $clientCNPJ.mask('00.000.000/0000-00', { reverse: true });
    var $clientCEP = $("#id_cep");
    $clientCEP.mask('00000-000', { reverse: true });
    var $clientBirthday = $("#id_data_aniversario");
    $clientBirthday.mask('00/00/0000', { reverse: true });
    var $clientTelefone = $("#id_telefone");
    $clientTelefone.mask('00 0000-0000', { reverse: true });
    var $clientCelular = $("#id_celular");
    $clientCelular.mask('00 00000-0000', { reverse: true });
});
$("#dropdown").on("click", function(e) {
    if ($(this).hasClass("open")) {
        $(this).removeClass("open");
        $(this).children("ul").slideUp("fast");
    } else {
        $(this).addClass("open");
        $(this).children("ul").slideDown("fast");
    }
})