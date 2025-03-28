/* Javascript for MyXBlock. */
function MyXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'save_question');
    var data = {};
    data['question'] = $('#question-input', element).val();
    $('#save-question-button',element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify(data),
            success: "updateCount"
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });

    var anshandlerUrl = runtime.handlerUrl(element, 'save_answer');
    var data = {};
    data['answer'] = $('#answer-input', element).val();
    $('#save-answer-button',element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: anshandlerUrl,
            data: JSON.stringify(data),
            success: "updateCount"
        });
    });
}
