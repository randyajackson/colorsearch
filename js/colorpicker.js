var colorPicker = new iro.ColorPicker("#colorWheel", {
    width: 290,
    height: 360,
    handleRadius: 8,
    handleUrl: null,
    handleOrigin: {y: 0, x: 0},
    borderWidth: 2,
    padding: 8,
    wheelLightness: true,
    layout: [
      {
        component: iro.ui.Wheel,
        options: {
        }
      },
      {
        component: iro.ui.Slider,
        options: {
        }
      }
    ]
  });

  colorPicker.on('color:change', function() {
      var rgbString = colorPicker.color.rgbString;
      rgbString = rgbString.replace('rgb', '');
      $('input[name=q]').val(rgbString);        
  })