/* ==================== NOTIFICATIONS ==================== */
function showNotification(message, type = 'info', duration = 4000) {
    const container = document.getElementById('notificationContainer');
    
    if (!container) return;
    
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    
    let icon = 'fa-info-circle';
    if (type === 'success') icon = 'fa-check-circle';
    if (type === 'error') icon = 'fa-exclamation-circle';
    if (type === 'warning') icon = 'fa-exclamation-triangle';
    
    notification.innerHTML = `
        <i class="fas ${icon}"></i>
        <span class="notification-text">${message}</span>
    `;
    
    container.appendChild(notification);
    
    // Auto remove notification
    setTimeout(() => {
        notification.style.animation = 'slideInRight 0.4s ease-out reverse';
        setTimeout(() => notification.remove(), 400);
    }, duration);
}

/* ==================== FORM HANDLING ==================== */
document.addEventListener('DOMContentLoaded', function() {
    // Navbar toggle
    const navbarToggle = document.getElementById('navbarToggle');
    const navbarMenu = document.getElementById('navbarMenu');
    
    if (navbarToggle) {
        navbarToggle.addEventListener('click', () => {
            navbarToggle.classList.toggle('active');
            navbarMenu.classList.toggle('active');
        });
        
        // Close menu when link is clicked
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navbarToggle.classList.remove('active');
                navbarMenu.classList.remove('active');
            });
        });
    }
    
    // Alert close buttons
    document.querySelectorAll('.alert-close').forEach(btn => {
        btn.addEventListener('click', function() {
            this.closest('.alert').style.display = 'none';
        });
    });
    
    // Dropdown toggle
    document.querySelectorAll('.dropdown').forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
            }
        });
    });
});

/* ==================== SELECT ELEMENT ENHANCEMENT ==================== */
document.addEventListener('DOMContentLoaded', function() {
    const selects = document.querySelectorAll('select.form-control');
    
    selects.forEach(select => {
        select.addEventListener('change', function() {
            this.style.color = this.value ? '#212121' : '#BDBDBD';
        });
        
        // Set initial color
        select.style.color = select.value ? '#212121' : '#BDBDBD';
    });
});

/* ==================== FORM VALIDATION ==================== */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validateUsername(username) {
    return username.length >= 3 && /^[a-zA-Z0-9_]+$/.test(username);
}

/* ==================== SMOOTH SCROLL ==================== */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

/* ==================== ANIMATION ON SCROLL ==================== */
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements with animation classes
document.querySelectorAll('.slide-up, .slide-down, .fade-in, .scale-in').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    observer.observe(el);
});

/* ==================== LOADING STATE ==================== */
function setLoadingState(button, isLoading) {
    if (isLoading) {
        button.disabled = true;
        button.style.opacity = '0.6';
        button.style.cursor = 'not-allowed';
    } else {
        button.disabled = false;
        button.style.opacity = '1';
        button.style.cursor = 'pointer';
    }
}

/* ==================== NUMBER INPUT ENHANCEMENT ==================== */
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('input[type="number"]').forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value === '') {
                this.style.borderColor = '#E0E0E0';
            }
        });
        
        input.addEventListener('focus', function() {
            this.style.borderColor = '#FFB03B';
        });
    });
});

/* ==================== CONFETTI ANIMATION (Optional) ==================== */
function createConfetti() {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '9999';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const confetti = [];
    const confettiCount = 50;
    
    class Confetti {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height - canvas.height;
            this.w = Math.random() * 10 + 5;
            this.h = Math.random() * 10 + 5;
            this.vx = Math.random() * 4 - 2;
            this.vy = Math.random() * 5 + 5;
            this.rotation = Math.random() * 360;
            this.color = ['#FFB03B', '#FF9800', '#FFC107', '#FF6F00'][Math.floor(Math.random() * 4)];
        }
        
        update() {
            this.x += this.vx;
            this.y += this.vy;
            this.rotation += 5;
            
            if (this.y > canvas.height) {
                return false;
            }
            return true;
        }
        
        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate((this.rotation * Math.PI) / 180);
            ctx.fillStyle = this.color;
            ctx.fillRect(-this.w / 2, -this.h / 2, this.w, this.h);
            ctx.restore();
        }
    }
    
    for (let i = 0; i < confettiCount; i++) {
        confetti.push(new Confetti());
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = confetti.length - 1; i >= 0; i--) {
            if (!confetti[i].update()) {
                confetti.splice(i, 1);
            } else {
                confetti[i].draw();
            }
        }
        
        if (confetti.length > 0) {
            requestAnimationFrame(animate);
        } else {
            canvas.remove();
        }
    }
    
    animate();
}

/* ==================== MODAL POPUP ==================== */
function showModal(title, message, confirmCallback = null) {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h2>${title}</h2>
                <button class="modal-close" onclick="this.closest('.modal-overlay').remove()">&times;</button>
            </div>
            <div class="modal-body">
                <p>${message}</p>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" onclick="this.closest('.modal-overlay').remove()">Close</button>
                ${confirmCallback ? '<button class="btn btn-primary" onclick="this.closest(\'.modal-overlay\').remove(); confirmCallback();">Confirm</button>' : ''}
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.remove();
        }
    });
}

/* ==================== KEYBOARD SHORTCUTS ==================== */
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K for search (optional)
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    }
    
    // Esc to close modals/dropdowns
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay').forEach(el => el.remove());
        document.querySelectorAll('.dropdown-menu.active').forEach(el => {
            el.classList.remove('active');
        });
    }
});

/* ==================== FETCH WITH ERROR HANDLING ==================== */
async function fetchWithErrorHandling(url, options = {}) {
    try {
        const response = await fetch(url, options);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        showNotification('An error occurred. Please try again.', 'error');
        throw error;
    }
}

/* ==================== LOCAL STORAGE HELPERS ==================== */
const Storage = {
    set: (key, value) => {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.warn('localStorage not available', e);
        }
    },
    
    get: (key) => {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : null;
        } catch (e) {
            console.warn('localStorage not available', e);
            return null;
        }
    },
    
    remove: (key) => {
        try {
            localStorage.removeItem(key);
        } catch (e) {
            console.warn('localStorage not available', e);
        }
    },
    
    clear: () => {
        try {
            localStorage.clear();
        } catch (e) {
            console.warn('localStorage not available', e);
        }
    }
};

/* ==================== DEBOUNCE FUNCTION ==================== */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/* ==================== TIMER UTILITY ==================== */
function startTimer(seconds, callback) {
    let remaining = seconds;
    
    const timer = setInterval(() => {
        remaining--;
        
        if (typeof callback === 'function') {
            callback(remaining);
        }
        
        if (remaining <= 0) {
            clearInterval(timer);
        }
    }, 1000);
    
    return timer;
}

/* ==================== COPY TO CLIPBOARD ==================== */
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Copied to clipboard!', 'success');
        }).catch(() => {
            fallbackCopy(text);
        });
    } else {
        fallbackCopy(text);
    }
}

function fallbackCopy(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    showNotification('Copied to clipboard!', 'success');
}

/* ==================== DEVICE DETECTION ==================== */
const DeviceInfo = {
    isMobile: () => /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent),
    isTablet: () => /iPad|Android/i.test(navigator.userAgent),
    isDesktop: () => !DeviceInfo.isMobile() && !DeviceInfo.isTablet()
};

/* ==================== PAGE VISIBILITY ==================== */
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        // Page is hidden
    } else {
        // Page is visible
    }
});

/* ==================== TOOLTIP ==================== */
function initializeTooltips() {
    document.querySelectorAll('[data-tooltip]').forEach(el => {
        el.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
            tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
            
            this.addEventListener('mouseleave', () => tooltip.remove());
        });
    });
}

/* ==================== PRINT FUNCTIONALITY ==================== */
function printPage() {
    window.print();
}

function exportAsJSON(data, filename = 'data.json') {
    const json = JSON.stringify(data, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    showNotification('File exported successfully!', 'success');
}

/* ==================== INITIALIZE ON DOM READY ==================== */
document.addEventListener('DOMContentLoaded', function() {
    initializeTooltips();
});
