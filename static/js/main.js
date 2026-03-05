/**
 * MarketAI Suite — Frontend JavaScript
 * Handles form submissions, loading states, and result rendering.
 */

// ─── Markdown to HTML Converter ───
function markdownToHTML(md) {
    if (!md) return '';
    let html = md;

    // Headings
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');

    // Bold & Italic
    html = html.replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>');
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

    // Unordered lists
    html = html.replace(/^[\-\*] (.+)$/gm, '<li>$1</li>');

    // Ordered lists
    html = html.replace(/^\d+\.\s(.+)$/gm, '<li>$1</li>');

    // Wrap consecutive <li> in <ul>
    html = html.replace(/((?:<li>.*?<\/li>\n?)+)/g, '<ul>$1</ul>');

    // Line breaks → paragraphs
    const blocks = html.split(/\n\n+/);
    html = blocks.map(block => {
        block = block.trim();
        if (!block) return '';
        if (/^<[hul]/.test(block)) return block;
        // Wrap plain text lines in <p>
        return block.split('\n').map(line => {
            line = line.trim();
            if (!line) return '';
            if (/^</.test(line)) return line;
            return `<p>${line}</p>`;
        }).join('');
    }).join('');

    return html;
}


// ─── Loading State ───
function showLoading(message) {
    const overlay = document.getElementById('loadingOverlay');
    const text = overlay.querySelector('.loading-text');
    text.textContent = message || 'AI is analyzing your data...';
    overlay.classList.add('active');
}

function hideLoading() {
    const overlay = document.getElementById('loadingOverlay');
    overlay.classList.remove('active');
}


// ─── Error Toast ───
function showError(message) {
    let toast = document.getElementById('errorToast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'errorToast';
        toast.className = 'error-toast';
        document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('active');
    setTimeout(() => toast.classList.remove('active'), 5000);
}


// ─── API Helper ───
async function postJSON(url, data) {
    const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
    const json = await response.json();
    if (!response.ok || json.error) {
        throw new Error(json.error || 'Something went wrong.');
    }
    return json.data;
}


// ─── Campaign Form ───
function initCampaignForm() {
    const form = document.getElementById('campaignForm');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;

        const data = {
            product: form.product.value.trim(),
            audience: form.audience.value.trim(),
            platform: form.platform.value.trim(),
        };

        showLoading('Generating your marketing campaign...');

        try {
            const result = await postJSON('/generate-campaign', data);
            displayResults('campaignResults', result.content, `Campaign for ${data.platform}`);
        } catch (err) {
            showError(err.message);
        } finally {
            hideLoading();
            btn.disabled = false;
        }
    });
}


// ─── Pitch Form ───
function initPitchForm() {
    const form = document.getElementById('pitchForm');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;

        const data = {
            product: form.product.value.trim(),
            persona: form.persona.value.trim(),
            industry: form.industry.value.trim(),
            company_size: form.company_size.value.trim(),
            budget: form.budget.value.trim(),
        };

        showLoading('Crafting your sales pitch...');

        try {
            const result = await postJSON('/generate-pitch', data);
            displayResults('pitchResults', result.content, `Pitch for ${data.industry}`);
        } catch (err) {
            showError(err.message);
        } finally {
            hideLoading();
            btn.disabled = false;
        }
    });
}


// ─── Lead Scoring Form ───
function initLeadForm() {
    const form = document.getElementById('leadForm');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;

        const data = {
            name: form.lead_name.value.trim(),
            budget: form.budget.value.trim(),
            need: form.need.value.trim(),
            urgency: form.urgency.value.trim(),
            authority: form.authority.value.trim(),
            notes: form.notes.value.trim(),
        };

        showLoading('Evaluating lead potential...');

        try {
            const result = await postJSON('/score-lead', data);
            displayLeadResults(result);
        } catch (err) {
            showError(err.message);
        } finally {
            hideLoading();
            btn.disabled = false;
        }
    });
}


// ─── Display Results ───
function displayResults(containerId, markdownContent, title) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const header = container.querySelector('.results-header h2');
    if (header) {
        header.innerHTML = `✨ ${title || 'AI Results'}`;
    }

    const content = container.querySelector('.results-content');
    if (content) {
        content.innerHTML = markdownToHTML(markdownContent);
    }

    container.classList.add('active');
    container.scrollIntoView({ behavior: 'smooth', block: 'start' });
}


// ─── Display Lead Results with Score Visualization ───
function displayLeadResults(result) {
    const container = document.getElementById('leadResults');
    if (!container) return;

    // Score circle
    const score = result.score ?? 0;
    const category = result.category || {};
    const color = category.color || '#6b7280';

    // dashoffset: 314 is full circle (circumference), 0 is empty
    const offset = 314 - (314 * score) / 100;

    const scoreHTML = `
        <div class="score-display">
            <div class="score-circle">
                <svg viewBox="0 0 120 120">
                    <circle class="track" cx="60" cy="60" r="50"></circle>
                    <circle class="progress" cx="60" cy="60" r="50"
                        style="stroke: ${color}; stroke-dashoffset: ${offset};"></circle>
                </svg>
                <div class="score-value" style="color: ${color};">
                    ${score}
                    <small>out of 100</small>
                </div>
            </div>
            <div class="score-info">
                <h3>${result.lead_name || 'Lead'}</h3>
                <span class="category-badge"
                      style="background: ${color}22; color: ${color}; border: 1px solid ${color}44;">
                    ${category.emoji || ''} ${category.label || 'N/A'}
                </span>
            </div>
        </div>
    `;

    container.querySelector('.results-header h2').innerHTML = '📊 Lead Evaluation Results';

    const content = container.querySelector('.results-content');
    content.innerHTML = scoreHTML + markdownToHTML(result.content);

    container.classList.add('active');
    container.scrollIntoView({ behavior: 'smooth', block: 'start' });
}


// ─── Mobile Nav Toggle ───
function initMobileNav() {
    const toggle = document.querySelector('.navbar-toggle');
    const links = document.querySelector('.navbar-links');
    if (toggle && links) {
        toggle.addEventListener('click', () => links.classList.toggle('open'));
    }
}


// ─── Init ───
document.addEventListener('DOMContentLoaded', () => {
    initMobileNav();
    initCampaignForm();
    initPitchForm();
    initLeadForm();
});
