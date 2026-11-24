// PERFORMANCE LINE CHART

const performance = document.getElementById('performanceChart');

new Chart(performance, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Average Performance',
            data: [55, 62, 68, 65, 78, 85],
            borderColor: '#9b7cff',
            backgroundColor: 'rgba(155,124,255,0.15)',
            fill: true,
            tension: 0.4,
            borderWidth: 3,
            pointRadius: 4
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                labels: { color: '#ffffff' }
            }
        },
        scales: {
            x: {
                ticks: { color: '#a5aec4' },
                grid: { color: '#29344e' }
            },
            y: {
                beginAtZero: true,
                max: 100,
                ticks: { color: '#a5aec4' },
                grid: { color: '#29344e' }
            }
        }
    }
});


// PERFORMANCE DISTRIBUTION

const distribution = document.getElementById('distributionChart');

new Chart(distribution, {
    type: 'doughnut',
    data: {
        labels: ['Excellent', 'Good', 'Average', 'Needs Support'],
        datasets: [{
            data: [30, 35, 25, 10],
            backgroundColor: [
                '#9b7cff',
                '#4f8cff',
                '#37c9a5',
                '#f5b95c'
            ],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    color: '#ffffff',
                    padding: 15
                }
            }
        }
    }
});