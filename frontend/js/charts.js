// Load Chart.js library dynamically (or include via CDN in admin_dashboard.html)
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
document.head.appendChild(script);

script.onload = () => {
    // Example data - Replace with API data from backend
    const degreeLabels = ['B.Tech', 'B.Sc', 'MCA', 'MBA', 'BBA'];
    const jobCounts = [50, 30, 20, 15, 10];

    const ctx1 = document.createElement('canvas');
    document.getElementById('chartsContainer').appendChild(ctx1);

    const degreeChart = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: degreeLabels,
            datasets: [{
                label: 'Number of Jobs per Degree',
                data: jobCounts,
                backgroundColor: 'rgba(38, 198, 218, 0.7)',
                borderColor: 'rgba(38, 198, 218, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true },
                title: {
                    display: true,
                    text: 'Job Opportunities per Degree'
                }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Pie chart example for job domain distribution
    const jobDomains = ['Software', 'Data Science', 'Management', 'Finance', 'Marketing'];
    const domainCounts = [40, 25, 20, 10, 5];

    const ctx2 = document.createElement('canvas');
    document.getElementById('chartsContainer').appendChild(ctx2);

    const domainChart = new Chart(ctx2, {
        type: 'pie',
        data: {
            labels: jobDomains,
            datasets: [{
                label: 'Job Domain Distribution',
                data: domainCounts,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Job Domain Distribution'
                }
            }
        }
    });
};
