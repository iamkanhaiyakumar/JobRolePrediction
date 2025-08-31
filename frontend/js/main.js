// Signup
document.getElementById('signupForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const res = await fetch('http://localhost:8000/signup', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, email, password})
    });
    const data = await res.json();
    document.getElementById('signupMessage').innerText = data.message;
});

// Login
document.getElementById('loginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email, password})
    });
    const data = await res.json();
    document.getElementById('loginMessage').innerText = data.message;
    if(data.token) {
        localStorage.setItem('token', data.token);
        window.location.href = 'profile.html';
    }
});

// // Education & Prediction
// document.getElementById('educationForm')?.addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const degree = document.getElementById('degree').value;
//     const specialization = document.getElementById('specialization').value;
//     const cgpa = document.getElementById('cgpa').value;
//     const certifications = document.getElementById('certifications').value;

//     const token = localStorage.getItem('token');
//     const res = await fetch('http://localhost:8000/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${token}`
//         },
//         body: JSON.stringify({degree, specialization, cgpa, certifications})
//     });

//     const data = await res.json();

//     // Save predictions in localStorage and redirect
//     if(data.predictions) {
//         localStorage.setItem('predictions', JSON.stringify(data.predictions));
//         window.location.href = 'prediction.html';
//     } else {
//         document.getElementById('predictionResult').innerText = "Prediction failed. Try again.";
//     }
// });


// Education & Prediction
document.getElementById('educationForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const Degree = document.getElementById('Degree').value;
    const Major = document.getElementById('Major').value;
    const CGPA = parseFloat(document.getElementById('CGPA').value);
    const Experience = parseFloat(document.getElementById('Experience').value);
    const Industry_Preference = document.getElementById('Industry_Preference').value;

    const token = localStorage.getItem('token');
    const res = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({Degree, Major, CGPA, Experience, Industry_Preference})
    });

    const data = await res.json();

    if(data.predictions){
        localStorage.setItem('predictions', JSON.stringify(data.predictions));
        window.location.href = 'prediction.html';
    } else {
        document.getElementById('predictionResult').innerText = "Prediction failed. Try again.";
    }
});
