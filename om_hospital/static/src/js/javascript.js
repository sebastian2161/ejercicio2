'use strict';
odoo.define('om_hospital.javascript', function (require) {
    require('web.dom_ready');
    var ajax = require('web.ajax');
     
        //$('#boton').prop('disabled', true);
    
        $('#boton').click(function(){
            alert('Mensaje esta OK');
    });
    
        $('#age').on('change', function(){
            let age = $('#age').val().trim();
            //alert(age.length);
            
            if(age < '18'){
                alert('La edad debe ser igual o mayor a 18 años');
                $('#age').val(18);
                return;
            }
    });
});