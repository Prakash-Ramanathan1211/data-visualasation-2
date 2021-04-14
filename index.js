document.addEventListener('DOMContentLoaded', () =>{
    Highcharts.chart('container', {
        xAxis: {
            categories: ['Apples', 'Bananas', 'Oranges']
        },
        series: [
            {
               name: 'John',
               data: [1,2,3]
            },
            {
                name: 'Jane',
                data: [2, 4, 8]
            }
        ]
    });
});