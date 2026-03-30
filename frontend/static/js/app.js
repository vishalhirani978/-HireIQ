// HireIQ Frontend JavaScript

// Accordion functionality
document.addEventListener('DOMContentLoaded', function() {
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(header => {
        header.addEventListener('click', function() {
            this.closest('.accordion-item').classList.toggle('active');
        });
    });
});

// Smooth transitions
const transitionElements = document.querySelectorAll('.card, .feature-card, .step-card');
transitionElements.forEach(el => {
    el.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-2px)';
    });
    el.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// Form validation feedback
const inputs = document.querySelectorAll('.form-input, .form-textarea');
inputs.forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    input.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
});

// Loading state management
function showLoading() {
    document.getElementById('loadingSpinner').style.display = 'block';
}

function hideLoading() {
    document.getElementById('loadingSpinner').style.display = 'none';
}

// API response handling
async function handleApiCall(url, data, successCallback) {
    try {
        showLoading();
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error('API request failed');
        }
        
        const result = await response.json();
        successCallback(result);
    } catch (error) {
        console.error('Error:', error);
        showError('An error occurred. Please try again.');
    } finally {
        hideLoading();
    }
}

// Error display
function showError(message) {
    const errorContainer = document.getElementById('errorContainer');
    if (errorContainer) {
        errorContainer.querySelector('span:last-child').textContent = message;
        errorContainer.classList.remove('hidden');
    }
}

// Success display
function showSuccess(message) {
    const successContainer = document.getElementById('successContainer');
    if (successContainer) {
        successContainer.querySelector('span:last-child').textContent = message;
        successContainer.classList.remove('hidden');
    }
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey || e.metaKey) {
        switch(e.key) {
            case '1':
                e.preventDefault();
                window.location.href = '/';
                break;
            case '2':
                e.preventDefault();
                window.location.href = '/cv-screening';
                break;
            case '3':
                e.preventDefault();
                window.location.href = '/dashboard';
                break;
            case '4':
                e.preventDefault();
                window.location.href = '/interview';
                break;
            case '5':
                e.preventDefault();
                window.location.href = '/bias-detector';
                break;
        }
    }
});

// Active navigation highlighting
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
    }
});
