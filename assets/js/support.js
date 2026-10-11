// Support form: accessible inline validation (including attachments), honeypot and Ajax submit.
// Without JavaScript the form posts directly to the configured endpoint.
(function () {
  var form = document.querySelector('[data-support-form]');
  if (!form || !form.getAttribute('action')) return; // Placeholder mode: nothing to enhance.

  var status = form.querySelector('[data-form-status]');
  var submit = form.querySelector('[data-submit]');
  var honeypot = form.querySelector('[name="' + form.getAttribute('data-honeypot') + '"]');
  var issueUrl = form.getAttribute('data-issue-url');
  var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var maxFiles = parseInt(form.getAttribute('data-max-files'), 10) || 3;
  var maxBytes = (parseFloat(form.getAttribute('data-max-file-mb')) || 10) * 1024 * 1024;
  var allowed = /\.(png|jpe?g|gif|webp|pdf|zip)$/i;
  form.setAttribute('novalidate', '');

  var rules = [
    { id: 'support-name', label: 'Name', check: function (v) { return v ? '' : 'Enter your name.'; } },
    { id: 'support-email', label: 'Email', check: function (v) {
      if (!v) return 'Enter your email address.';
      return emailPattern.test(v) ? '' : 'Enter an email address like name@example.com.';
    } },
    { id: 'support-topic', label: 'Topic', check: function (v) { return v ? '' : 'Choose a topic.'; } },
    { id: 'support-message', label: 'Message', check: function (v) { return v ? '' : 'Enter your message.'; } },
    { id: 'support-files', label: 'Files', check: function () { return checkFiles(document.getElementById('support-files')); } }
  ];

  function checkFiles(input) {
    var files = input && input.files ? Array.prototype.slice.call(input.files) : [];
    if (files.length > maxFiles) return 'Attach up to ' + maxFiles + ' files. You chose ' + files.length + '.';
    for (var i = 0; i < files.length; i++) {
      if (!allowed.test(files[i].name)) return files[i].name + ' isn\'t a PNG, JPG, GIF, WebP, PDF or ZIP file.';
      if (files[i].size > maxBytes) return files[i].name + ' is larger than ' + (maxBytes / 1048576) + ' MB.';
    }
    return '';
  }

  function setError(field, message) {
    var error = document.getElementById(field.id + '-error');
    if (message) {
      field.setAttribute('aria-invalid', 'true');
      error.textContent = message;
      error.hidden = false;
    } else {
      field.removeAttribute('aria-invalid');
      error.textContent = '';
      error.hidden = true;
    }
  }

  function showStatus(type, html) {
    status.className = 'form-status form-status--' + type;
    status.setAttribute('role', type === 'error' ? 'alert' : 'status');
    status.innerHTML = html;
    status.hidden = false;
    status.focus();
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }

  function validate() {
    var problems = [];
    rules.forEach(function (rule) {
      var field = document.getElementById(rule.id);
      var message = rule.check(field.value.trim());
      setError(field, message);
      if (message) problems.push({ id: rule.id, message: message });
    });
    return problems;
  }

  // Clear a field's error as soon as it's fixed.
  rules.forEach(function (rule) {
    var field = document.getElementById(rule.id);
    field.addEventListener('change', function () {
      // Files are checked as soon as they're chosen; other fields once they've been flagged.
      if (field.type === 'file' || field.getAttribute('aria-invalid') === 'true') setError(field, rule.check(field.value.trim()));
      // Once every problem is fixed, the error summary is out of date: hide it.
      if (status.classList.contains('form-status--error') && !form.querySelector('[aria-invalid="true"]')) status.hidden = true;
    });
  });

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    var problems = validate();
    if (problems.length) {
      var items = problems.map(function (p) {
        return '<li><a href="#' + p.id + '">' + escapeHtml(p.message) + '</a></li>';
      }).join('');
      showStatus('error', '<p><strong>Please fix ' + (problems.length === 1 ? '1 problem' : problems.length + ' problems') + ':</strong></p><ul>' + items + '</ul>');
      return;
    }
    // Spam bots fill in the hidden honeypot. Pretend it worked and send nothing.
    if (honeypot && honeypot.value) {
      form.reset();
      showStatus('success', '<p><strong>Thanks, your message has been sent.</strong></p>');
      return;
    }
    status.hidden = true;
    submit.disabled = true;
    submit.textContent = 'Sending…';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (response) {
        if (!response.ok) { var err = new Error('HTTP ' + response.status); err.status = response.status; throw err; }
        form.reset();
        showStatus('success', '<p><strong>Thanks, your message has been sent.</strong> We\'ll reply to the email address you gave us.</p>');
      })
      .catch(function (err) {
        if (err && err.status === 413) {
          showStatus('error', '<p><strong>Your files are too large to send.</strong> Try smaller or fewer files, or send the message without them and we\'ll ask for them by email.</p>');
          return;
        }
        showStatus('error', '<p><strong>Sorry, your message couldn\'t be sent.</strong> Please try again, or <a href="' + issueUrl + '">open a support request on GitHub</a>.</p>');
      })
      .then(function () {
        submit.disabled = false;
        submit.textContent = 'Send message';
      });
  });

  status.addEventListener('click', function (event) {
    var link = event.target.closest('a[href^="#"]');
    if (!link) return;
    event.preventDefault();
    var target = document.getElementById(link.getAttribute('href').slice(1));
    if (target) target.focus();
  });
})();
