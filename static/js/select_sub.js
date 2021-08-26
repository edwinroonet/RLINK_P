function ss_write(obj) {

    var strHtml = "";

    strHtml = '<select id="' + obj.sid + '" name="' + obj.snm + '" onchange="' + obj.onchange + '" style="' + obj.style + '">';
    for (var idx in obj.data) {
        var title = '';
        try {
            title = obj.title[idx];
        } catch (e) {
            try {
                title = obj.data[idx];
            } catch (e) {
                title = '';
            }
        }
        var sValue = '';
        try {
            sValue = obj.data[idx];
        } catch (e) {
            sValue = '';
        }

        strHtml += '<option value="' + sValue + '" ' + ((obj.select == sValue) ? ' selected' : '') + '>' + title + '</option>';
    }
    strHtml += '</select>';

    $('form[name=' + obj.fnm + ']').append(strHtml);
    //$('#' + obj.sid).select();
}
