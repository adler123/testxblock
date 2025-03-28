/* Javascript for MyXBlock. */
function MyXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });

    function saveQuestion() {
        var saveqsurl=runtime.handlerUrl(element, 'save_question');
        $.ajax({
            type: "POST",
            url: saveqsurl,
            data: JSON.stringify({"hello": "world"}),
            success: "updateCount"
        });
        
        alert('Câu hỏi đã được lưu!');
    }
}
