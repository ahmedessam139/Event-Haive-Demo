// Get form elements
const $form = $('.form-container');
const $nameInput = $('#name');
const $mobileInput = $('#mobile');
const $emailInput = $('#email');
const $nationalIdInput = $('#national-id');

// Add event listener to form submission
$form.on('submit', async function (event) {
    // Prevent form from submitting
    event.preventDefault();


    // Validate mobile number
    const mobileRegex = /^01\d{9}$/;
    if (!mobileRegex.test($mobileInput.val())) {
        alert('Mobile number must start with "01" and be 11 digits');
        return;
    }



    // All validation passed, fetch API and put data in object
    const user_info = {
        mobile: $mobileInput.val(),
        Id: $nationalIdInput.val()
    };

    // Fetch API and use data object
    response = await send_user(user_info);

    console.log(response.status);
    if (response.status == "ok") {       
        ticket_url = response.ticket.value;
        console.log(ticket_url);
        event_instructions = `--------Event Instructions--------

Dear Attendee💙,\n
        
-Please note that the link to your ticket will expire‼️ in two days, so it is necessary to *save it as a screenshot on your device* for easy access during the event.
        
-Additionally, please ensure that you have your ticket with you at all times throughout the event. This will help us maintain a secure and organized environment for all attendees.
        
-If you have any questions or concerns, please do not hesitate to contact us at +201111486231. 

-Thank you for your cooperation, and we look forward to seeing you at our event!

📌Reminder, all the event details are on the ticket
        
Your Ticket:`;

        $('.form-container').empty();
        $('.form-container').append(`<a href="${ticket_url}">${ticket_url}</a>`)
        $('.form-container').append('<input value="Send To Whatsapp" id="send-btn" />');
        $('.form-container').append('<input value="Register again" id="back-btn" />');
        $('.form-container').css('width', 'auto'); // Set the width to auto



        // Construct the WhatsApp URL with the user's phone number and message
        const whatsapp_url = `https://wa.me/+2${$mobileInput.val()}?text=${encodeURIComponent(`${event_instructions}\n${ticket_url}\n©️E-Tickets Managed by *Event Hive*`)}`;

        $('#send-btn').on('click', function () {
            // Redirect to the WhatsApp URL
            window.location.href = whatsapp_url;
        });
        $('#back-btn').on('click', function () {
            location.reload();
        });

    }
    if (response.status != "ok") {
        alert(response.status);
    }




});



async function send_user(user_info) {
    var respose_data;
    await fetch(`add_user_by_number`, {
        method: "POST",
        headers: {
            "accept": "application/json"
        },
        body: JSON.stringify(user_info)
    }).then(res => res.json())
        .then(data => {
            respose_data = data;
        }
        );
    return respose_data;
}


