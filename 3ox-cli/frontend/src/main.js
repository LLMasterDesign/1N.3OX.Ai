/**
 * 3OX Floating Bar UI
 * Command bridge interface for 3OX CLI system
 */

class ThreeOXBar {
    constructor() {
        this.apiBase = 'http://127.0.0.1:8000';
        this.currentJob = null;
        this.isProcessing = false;
        this.init();
    }

    init() {
        this.createUI();
        this.setupEventListeners();
        this.loadHistory();
    }

    createUI() {
        // Create main container
        const container = document.createElement('div');
        container.id = 'threeox-container';
        container.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 600px;
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 12px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            border: 1px solid #333;
            z-index: 10000;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: none;
        `;

        // Create header
        const header = document.createElement('div');
        header.style.cssText = `
            padding: 12px 16px;
            border-bottom: 1px solid #333;
            display: flex;
            align-items: center;
            justify-content: space-between;
        `;

        const title = document.createElement('div');
        title.textContent = '3OX Command Bridge';
        title.style.cssText = `
            color: #00ff88;
            font-weight: 600;
            font-size: 14px;
        `;

        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '×';
        closeBtn.style.cssText = `
            background: none;
            border: none;
            color: #888;
            font-size: 18px;
            cursor: pointer;
            padding: 0;
            width: 24px;
            height: 24px;
        `;
        closeBtn.onclick = () => this.hide();

        header.appendChild(title);
        header.appendChild(closeBtn);

        // Create role selector
        const roleContainer = document.createElement('div');
        roleContainer.style.cssText = `
            padding: 8px 16px;
            border-bottom: 1px solid #333;
        `;

        const roleLabel = document.createElement('label');
        roleLabel.textContent = 'Role:';
        roleLabel.style.cssText = `
            color: #ccc;
            font-size: 12px;
            margin-right: 8px;
        `;

        const roleSelect = document.createElement('select');
        roleSelect.id = 'role-select';
        roleSelect.style.cssText = `
            background: #333;
            border: 1px solid #555;
            color: #fff;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
        `;

        const roles = [
            { value: '@MASTER', label: 'Master' },
            { value: '@SENTINEL', label: 'Sentinel' },
            { value: '@LIGHTHOUSE', label: 'Lighthouse' },
            { value: '@ALCHEMIST', label: 'Alchemist' },
            { value: '@BRIDGE', label: 'Bridge' }
        ];

        roles.forEach(role => {
            const option = document.createElement('option');
            option.value = role.value;
            option.textContent = role.label;
            roleSelect.appendChild(option);
        });

        roleContainer.appendChild(roleLabel);
        roleContainer.appendChild(roleSelect);

        // Create input area
        const inputContainer = document.createElement('div');
        inputContainer.style.cssText = `
            padding: 16px;
        `;

        const input = document.createElement('input');
        input.type = 'text';
        input.id = 'command-input';
        input.placeholder = 'Enter 3OX command... (e.g., organize ~/Pictures, summarize ~/Documents)';
        input.style.cssText = `
            width: 100%;
            padding: 12px 16px;
            background: #222;
            border: 1px solid #444;
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
            outline: none;
            box-sizing: border-box;
        `;

        inputContainer.appendChild(input);

        // Create options
        const optionsContainer = document.createElement('div');
        optionsContainer.style.cssText = `
            padding: 8px 16px;
            display: flex;
            gap: 16px;
            align-items: center;
        `;

        const sensitiveCheckbox = document.createElement('label');
        sensitiveCheckbox.style.cssText = `
            color: #ccc;
            font-size: 12px;
            display: flex;
            align-items: center;
            gap: 4px;
        `;

        const sensitiveInput = document.createElement('input');
        sensitiveInput.type = 'checkbox';
        sensitiveInput.id = 'sensitive-checkbox';
        sensitiveInput.style.margin = '0';

        sensitiveCheckbox.appendChild(sensitiveInput);
        sensitiveCheckbox.appendChild(document.createTextNode('Sensitive'));

        const onlineCheckbox = document.createElement('label');
        onlineCheckbox.style.cssText = `
            color: #ccc;
            font-size: 12px;
            display: flex;
            align-items: center;
            gap: 4px;
        `;

        const onlineInput = document.createElement('input');
        onlineInput.type = 'checkbox';
        onlineInput.id = 'online-checkbox';
        onlineInput.style.margin = '0';

        onlineCheckbox.appendChild(onlineInput);
        onlineCheckbox.appendChild(document.createTextNode('Allow Online'));

        optionsContainer.appendChild(sensitiveCheckbox);
        optionsContainer.appendChild(onlineCheckbox);

        // Create status area
        const statusContainer = document.createElement('div');
        statusContainer.id = 'status-container';
        statusContainer.style.cssText = `
            padding: 8px 16px;
            min-height: 20px;
            font-size: 12px;
            color: #888;
        `;

        // Create history area
        const historyContainer = document.createElement('div');
        historyContainer.id = 'history-container';
        historyContainer.style.cssText = `
            max-height: 200px;
            overflow-y: auto;
            border-top: 1px solid #333;
            padding: 8px 0;
        `;

        // Assemble UI
        container.appendChild(header);
        container.appendChild(roleContainer);
        container.appendChild(inputContainer);
        container.appendChild(optionsContainer);
        container.appendChild(statusContainer);
        container.appendChild(historyContainer);

        document.body.appendChild(container);
        this.container = container;
        this.input = input;
        this.roleSelect = roleSelect;
        this.sensitiveCheckbox = sensitiveInput;
        this.onlineCheckbox = onlineInput;
        this.statusContainer = statusContainer;
        this.historyContainer = historyContainer;
    }

    setupEventListeners() {
        // Show/hide on Ctrl+Space
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.code === 'Space') {
                e.preventDefault();
                this.toggle();
            }
        });

        // Handle Enter key
        this.input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !this.isProcessing) {
                this.submitCommand();
            }
        });

        // Handle Escape key
        this.input.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.hide();
            }
        });

        // Focus input when shown
        this.container.addEventListener('click', (e) => {
            if (e.target === this.container || e.target.closest('#command-input')) {
                this.input.focus();
            }
        });
    }

    toggle() {
        if (this.container.style.display === 'none') {
            this.show();
        } else {
            this.hide();
        }
    }

    show() {
        this.container.style.display = 'block';
        this.input.focus();
        this.loadHistory();
    }

    hide() {
        this.container.style.display = 'none';
        this.input.value = '';
        this.isProcessing = false;
    }

    async submitCommand() {
        const command = this.input.value.trim();
        if (!command) return;

        const role = this.roleSelect.value;
        const sensitive = this.sensitiveCheckbox.checked;
        const allowOnline = this.onlineCheckbox.checked;

        this.isProcessing = true;
        this.updateStatus('Processing command...', 'info');

        try {
            const response = await fetch(`${this.apiBase}/api/3oxjob`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    role,
                    prompt: command,
                    targets: this.extractTargets(command),
                    sensitive,
                    allow_online: allowOnline
                })
            });

            const data = await response.json();

            if (data.requires_confirmation) {
                this.handleConfirmation(data);
            } else {
                this.handleJobSubmission(data);
            }

        } catch (error) {
            this.updateStatus(`Error: ${error.message}`, 'error');
            console.error('Command submission error:', error);
        } finally {
            this.isProcessing = false;
        }
    }

    extractTargets(command) {
        // Simple target extraction - look for paths starting with ~ or /
        const pathRegex = /[~\/][^\s]+/g;
        return command.match(pathRegex) || [];
    }

    handleJobSubmission(data) {
        this.currentJob = data.job_id;
        this.updateStatus(`Job ${data.job_id} submitted: ${data.message}`, 'success');
        this.addToHistory(command, data.job_id);
        
        // Poll for job completion
        this.pollJobStatus(data.job_id);
    }

    handleConfirmation(data) {
        this.updateStatus(`Confirmation required: ${data.confirmation_message}`, 'warning');
        
        // In a real implementation, show confirmation dialog
        const confirmed = confirm(data.confirmation_message);
        if (confirmed) {
            this.confirmJob(data.job_id);
        }
    }

    async confirmJob(jobId) {
        try {
            const response = await fetch(`${this.apiBase}/api/confirm/${jobId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ confirmed: true })
            });

            const data = await response.json();
            this.updateStatus(data.message, 'success');
            this.pollJobStatus(jobId);

        } catch (error) {
            this.updateStatus(`Confirmation error: ${error.message}`, 'error');
        }
    }

    async pollJobStatus(jobId) {
        const maxAttempts = 30; // 30 seconds max
        let attempts = 0;

        const poll = async () => {
            try {
                const response = await fetch(`${this.apiBase}/api/job/${jobId}`);
                const data = await response.json();

                if (data.status === 'COMPLETED') {
                    this.updateStatus(`Job completed: ${data.result_data?.message || 'Success'}`, 'success');
                    this.showJobResult(data);
                    return;
                } else if (data.status === 'FAILED') {
                    this.updateStatus(`Job failed: ${data.error_message || 'Unknown error'}`, 'error');
                    return;
                } else {
                    this.updateStatus(`Job status: ${data.status}`, 'info');
                }

                attempts++;
                if (attempts < maxAttempts) {
                    setTimeout(poll, 1000);
                } else {
                    this.updateStatus('Job timeout - check status manually', 'warning');
                }

            } catch (error) {
                this.updateStatus(`Status check error: ${error.message}`, 'error');
            }
        };

        poll();
    }

    showJobResult(data) {
        // Create result display
        const resultDiv = document.createElement('div');
        resultDiv.style.cssText = `
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 12px;
            margin: 8px 16px;
            font-size: 12px;
            color: #ccc;
        `;

        resultDiv.innerHTML = `
            <div style="color: #00ff88; font-weight: bold; margin-bottom: 8px;">Job Result:</div>
            <pre style="white-space: pre-wrap; margin: 0;">${JSON.stringify(data.result_data, null, 2)}</pre>
        `;

        this.historyContainer.appendChild(resultDiv);
        this.historyContainer.scrollTop = this.historyContainer.scrollHeight;
    }

    updateStatus(message, type = 'info') {
        const colors = {
            info: '#888',
            success: '#00ff88',
            warning: '#ffaa00',
            error: '#ff4444'
        };

        this.statusContainer.textContent = message;
        this.statusContainer.style.color = colors[type] || colors.info;
    }

    addToHistory(command, jobId) {
        const historyItem = document.createElement('div');
        historyItem.style.cssText = `
            padding: 8px 16px;
            border-bottom: 1px solid #333;
            font-size: 12px;
            color: #ccc;
            cursor: pointer;
        `;

        historyItem.innerHTML = `
            <div style="color: #00ff88;">${command}</div>
            <div style="color: #666; font-size: 10px;">Job: ${jobId}</div>
        `;

        historyItem.onclick = () => {
            this.input.value = command;
            this.input.focus();
        };

        this.historyContainer.insertBefore(historyItem, this.historyContainer.firstChild);

        // Limit history to 10 items
        while (this.historyContainer.children.length > 10) {
            this.historyContainer.removeChild(this.historyContainer.lastChild);
        }
    }

    loadHistory() {
        // Load command history from localStorage
        const history = JSON.parse(localStorage.getItem('threeox-history') || '[]');
        this.historyContainer.innerHTML = '';

        history.forEach(item => {
            this.addToHistory(item.command, item.jobId);
        });
    }

    saveHistory(command, jobId) {
        const history = JSON.parse(localStorage.getItem('threeox-history') || '[]');
        history.unshift({ command, jobId, timestamp: Date.now() });
        
        // Keep only last 50 items
        const limitedHistory = history.slice(0, 50);
        localStorage.setItem('threeox-history', JSON.stringify(limitedHistory));
    }
}

// Initialize the 3OX Bar when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ThreeOXBar();
});

// Also initialize if DOM is already loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new ThreeOXBar();
    });
} else {
    new ThreeOXBar();
}