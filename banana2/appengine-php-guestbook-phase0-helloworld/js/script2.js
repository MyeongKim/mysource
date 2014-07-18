$(document).ready(function(){
    // email check

    // focus out 
    $('#test').focusout(function() {
        // alert('b');
        // $('#test').val('');
        // $('#test').focus();
        // checkEmail();
        checkEmail2();
    });

    function checkEmail2() {
        var inputEmail = $('#test').val();
        var email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;

            if(!email_regex.test(inputEmail)){
                alert('false');
            } else {
                alert('true');
            }
    }

    // email validate
    function checkEmail() {
        var email = $('#test').val();
        // start to 0 
        var firstIndex = email.indexOf('@'); 
        var secondIndex = email.indexOf('.'); 

        // if @ or . is not // do not first
        if(firstIndex < 1 || secondIndex < 1) {
            alert('Please input email.')
            $('#test').val('');
            return;
        } 

        // slice(a, b) : a <= [str] < b
        // slice(a) : a ~ [end]
        var emailAddr = email.slice(0, firstIndex);
        var emailComp = email.slice(firstIndex, secondIndex);
        var emailDomain = email.slice(secondIndex);

        //alert(firstIndex + '\n' + secondIndex);
    }
    // email check end

    // checkbox enter (assignment 2, 3)
    $('#test2').keypress(function(event){

        if(event.which == 13){
            if ($('#checksample').is(":checked")){
                alert('Thank you!');
            }
        } else{

        }
    });

    $('#name').keypress(function(event){
        if(event.which == 13){
            alert($('#name').val());

        }
    });



    $('#test').keypress(function(event){
        if(event.which == 13){
            alert($('#test').val());

        }
    });



    $('#test2').keypress(function(event){
        if(event.which == 13){
            alert($('#test2').val());

        }
    });
    // checkbox enter change end


    $(".accordion").accordion({heightStyle: "fill" });



    $(".thumb1").click(function(){
        $("#dialog").dialog();

    });



    // nav bar anchor

    function scroll_if_anchor(href) {
        href = typeof(href) == "string" ? href : $(this).attr("href");
        
        // You could easily calculate this dynamically if you prefer
        var fromTop = 50;
        
        // If our Href points to a valid, non-empty anchor, and is on the same page (e.g. #foo)
        // Legacy jQuery and IE7 may have issues: http://stackoverflow.com/q/1593174
        if(href.indexOf("#") == 0) {
            var $target = $(href);
            
            // Older browser without pushState might flicker here, as they momentarily
            // jump to the wrong position (IE < 10)
            if($target.length) {
                $('html, body').animate({ scrollTop: $target.offset().top - fromTop });
                if(history && "pushState" in history) {
                    history.pushState({}, document.title, window.location.pathname + href);
                    return false;
                }
            }
        }
    }    

    // When our page loads, check to see if it contains and anchor
    scroll_if_anchor(window.location.hash);

    // Intercept all anchor clicks
    $("body").on("click", "a", scroll_if_anchor);




    // nav bar anchor end

       
    // hover opacity

    $('.portfolio-link').hover(function() { 
        $('img', this).stop().animate({"opacity": 0.5}); 
    },function() { 
        $('img', this).stop().animate({"opacity": 1}); 
    });

    // hover opacity



    // email @@ check

    function validateForm() {
        var x = document.form["email"].value;
        var atpos = x.indexOf("@");
        var dotpos = x.lastIndexOf(".");
        if (atpos< 1 || dotpos<atpos+2 || dotpos+2>=x.length) {

            x='';
            return false;   

        };
    };

    // email @@ check end





});


