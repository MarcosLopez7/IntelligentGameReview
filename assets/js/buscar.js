/**
 * Created by marcoslopez7 on 5/05/16.
 */

function buscar(){
    var texto = $('#nombre').val();

    window.location.replace('/listgame/?texto=' + texto)
}