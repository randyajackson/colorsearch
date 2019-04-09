$(function () {
    $('#supported').text('Supported/allowed: ' + !!screenfull.enabled);

    if (!screenfull.enabled) {
        return false;
    }

    $('.effect-milo').click(function () {
        screenfull.request(this);
    });

    function fullscreenchange() {
        var elem = screenfull.element;

        $('#status').text('Is fullscreen: ' + screenfull.isFullscreen);

        if (elem) {
            $('#element').text('Element: ' + elem.localName + (elem.id ? '#' + elem.id : ''));
        }

        if (!screenfull.isFullscreen) {
            $('#external-iframe').remove();
            document.body.style.overflow = 'auto';
        }
    }

    screenfull.on('change', fullscreenchange);

    // Set the initial values
    fullscreenchange();
});