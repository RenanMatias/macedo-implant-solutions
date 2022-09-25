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
    var $clientTelefone = $("#id_telefone");
    $clientTelefone.mask('00 0000-0000', { reverse: true });
    var $clientCelular = $("#id_celular");
    $clientCelular.mask('00 00000-0000', { reverse: true });

    $("#id_cnpj").parent("div").addClass("hidden");
    $("#id_cro").parent("div").addClass("hidden");
    $("#id_cro_uf").parent("div").addClass("hidden");
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

$("#id_tipo").change(function() {
    if (this.value == "Dentista") {
        $("#id_cpf").parent("div").removeClass("hidden");
        $("#id_cnpj").parent("div").removeClass("hidden");
        $("#id_cro").parent("div").removeClass("hidden");
        $("#id_cro_uf").parent("div").removeClass("hidden");
    } else if (this.value == "Paciente") {
        $("#id_cpf").parent("div").removeClass("hidden");
        $("#id_cnpj").parent("div").addClass("hidden");
        $("#id_cro").parent("div").addClass("hidden");
        $("#id_cro_uf").parent("div").addClass("hidden");
    } else if (this.value == "Instituição") {
        $("#id_cpf").parent("div").addClass("hidden");
        $("#id_cnpj").parent("div").removeClass("hidden");
        $("#id_cro").parent("div").addClass("hidden");
        $("#id_cro_uf").parent("div").addClass("hidden");
    }
})

$(":input#id_cep").focusout(function(e) {
    const cep = this.value

    $.get('https://viacep.com.br/ws/' + cep + '/json', function(data) {
        if (data.erro != 'true') {
            $('#id_endereco').val(data.logradouro)
            $('#id_complemento').val(data.complemento)
            $('#id_bairro').val(data.bairro)
            $('#id_cidade').val(data.localidade)
            $('#id_uf').val(data.uf)
        } else {
            $('#id_endereco').val('')
            $('#id_complemento').val('')
            $('#id_bairro').val('')
            $('#id_cidade').val('')
            $('#id_uf').val('')
        }
    })

})