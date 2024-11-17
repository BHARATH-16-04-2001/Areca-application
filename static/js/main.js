$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#remedi').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
                $('#remedi').hide();
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result

                alert(data);

                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text(' Result:  ' + data);
                $('#remedi').fadeIn(600);
                if(data=="Bud Borer Disease")
                {
                    $("#remedi").html("<h1>Remedies:</h1><h2>Bud Borer Disease</h2>Bordeaux mixture: After removing affected tissues, smear with 10% Bordeaux paste.Terra Fungicide: A biological product for managing bud rot");
                }
                else if(data=="Yellow Leaf Disease")
                {
                    $("#remedi").html("<h1>Remedies:</h1><h2>Yellow Leaf Disease</h2>Application of additional dose of superphosphate (1 Kg/palm) alone or in combination with lime (I Kg/palm). Manuring with green leaf and compost @ 12 Kg each/palm. Irrigation at four days interval during summer months.");
                }
                else if(data=="Mahali Koleroga Disease")
                {
                    $("#remedi").html("<h1>Remedies:</h1><h2>Mahali Koleroga Disease</h2>Dissolve 1 kg of Copper Sulphate in 50 litres of water and kg of lime in 50 litres of water separately and mix just before spraying. If the quality of lime is inferior, 1 kg of lime may not be sufficient to neutralise the copper sulphate.");
                }
                else if(data=="Stem Cracking Disease")
                {
                    $("#remedi").html("<h1>Remedies:</h1><h2>Stem Cracking Disease</h2>Borax: Spray 2 grams of borax per liter of water on bunches in the early stages of the disease. K2O: Apply K2O at the base to prevent nut splitting.Drainage: Improve drainage facilities in the garden. Irrigation: Provide regular irrigation during drought.Root feeding: Feed roots with Hexaconazole5EC at 2% (100 ml solution per palm) at quarterly intervals.")  
                }
                else if(data=="Stem Bleeding Disease")
                {
                    $("#remedi").html("<h1>Remedies:</h1><h2>Stem Bleeding Disease</h2>Complete removal of the disease affected tissues using a chisel and smearing the chiselled portion with hexaconazole (0.2%) is also recommended. Coal tar should be applied after 1-2 days on the treated portion. Destroy the chiselled diseased tissues by burning.")
                }

                else{
                    $("#remedi").html("<h1>No problem found</h1>")

                }
            },
        });
    });

});
