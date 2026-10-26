import React, { useState } from 'react';
import { AlertOctagon, CheckCircle2, ShieldAlert, Clock } from 'lucide-react';

export default function IncidentTask({ onComplete }) {
  const [formData, setFormData] = useState({
    severity: 'P2 - High',
    service: 'Payment Gateway',
    title: '',
    resolution: '',
    status: 'Resolved',
  });

  const [submittedData, setSubmittedData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title || !formData.resolution) return;

    const incId = `INC-${Math.floor(1000 + Math.random() * 9000)}`;

    const completedRecord = {
      id: incId,
      type: 'IT Incident',
      title: `${formData.severity.split(' ')[0]}: ${formData.title}`,
      details: `${formData.service} • Status: ${formData.status} • "${formData.resolution}"`,
      timestamp: new Date().toLocaleTimeString(),
      status: formData.status,
      metadata: {
        ...formData,
        incId,
        resolvedAt: new Date().toLocaleTimeString(),
      },
    };

    setSubmittedData(completedRecord);
    if (onComplete) onComplete(completedRecord);
  };

  const handleReset = () => {
    setSubmittedData(null);
    setFormData({
      severity: 'P2 - High',
      service: 'Payment Gateway',
      title: '',
      resolution: '',
      status: 'Resolved',
    });
  };

  const getSeverityBadgeClass = (sev) => {
    if (sev.startsWith('P1')) return 'bg-rose-100 text-rose-800 border-rose-300';
    if (sev.startsWith('P2')) return 'bg-amber-100 text-amber-800 border-amber-300';
    return 'bg-blue-100 text-blue-800 border-blue-300';
  };

  return (
    <div className="task-card">
      <div className="task-header">
        <div className="task-icon-wrapper bg-rose-100 text-rose-600">
          <AlertOctagon size={24} />
        </div>
        <div>
          <h2 className="task-title">Task 3: IT Incident & Support Triage</h2>
          <p className="task-subtitle">Log, triage, and record resolution for infrastructure service outages</p>
        </div>
      </div>

      {submittedData ? (
        <div className="result-box border-rose-200 bg-rose-50/40" data-testid="incident-success-card">
          <div className="flex items-center gap-2 text-rose-800 font-semibold mb-3">
            <CheckCircle2 size={20} className="text-emerald-600" />
            <span>Incident Logged & Updated</span>
          </div>

          <div className="incident-card">
            <div className="flex justify-between items-center mb-2">
              <span
                className={`text-xs px-2 py-0.5 rounded-full font-bold border ${getSeverityBadgeClass(
                  submittedData.metadata.severity
                )}`}
              >
                {submittedData.metadata.severity}
              </span>
              <span className="font-mono text-sm font-bold text-gray-700">
                {submittedData.id}
              </span>
            </div>

            <h3 className="text-base font-bold text-gray-900 mb-1">
              {submittedData.metadata.title}
            </h3>
            <p className="text-xs font-semibold text-gray-500 mb-3">
              Affected Component: {submittedData.metadata.service}
            </p>

            <div className="bg-white p-3 rounded border border-gray-200 text-xs text-gray-700 mb-3">
              <span className="font-semibold block mb-1 text-gray-900">Resolution Applied:</span>
              {submittedData.metadata.resolution}
            </div>

            <div className="text-xs text-gray-500 flex justify-between pt-2 border-t border-gray-200">
              <span className="flex items-center gap-1">
                <Clock size={12} /> Logged: {submittedData.metadata.resolvedAt}
              </span>
              <span className="font-semibold text-emerald-700">
                State: {submittedData.metadata.status}
              </span>
            </div>
          </div>

          <button onClick={handleReset} className="btn-secondary mt-4 w-full">
            Log Another Incident
          </button>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="task-form">
          <div className="grid-2">
            <div className="form-group">
              <label htmlFor="incident-severity">Severity Level</label>
              <select
                id="incident-severity"
                data-testid="incident-severity"
                value={formData.severity}
                onChange={(e) => setFormData({ ...formData, severity: e.target.value })}
                className="form-input"
              >
                <option value="P1 - Critical">P1 - Critical (Outage / Revenue Impact)</option>
                <option value="P2 - High">P2 - High (Degraded Performance)</option>
                <option value="P3 - Normal">P3 - Normal (Minor Bug / Non-blocking)</option>
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="incident-service">Affected Service</label>
              <select
                id="incident-service"
                data-testid="incident-service"
                value={formData.service}
                onChange={(e) => setFormData({ ...formData, service: e.target.value })}
                className="form-input"
              >
                <option value="Payment Gateway">Payment Gateway & Billing</option>
                <option value="User Authentication">User Authentication (OAuth / JWT)</option>
                <option value="PostgreSQL Cluster">Primary Database Cluster</option>
                <option value="Cloud CDN">Edge Routing & CDN</option>
                <option value="Order Processing">Order Fulfillment Service</option>
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="incident-title">Incident Title *</label>
            <input
              id="incident-title"
              data-testid="incident-title"
              type="text"
              required
              placeholder="e.g. Payment Gateway 502 Bad Gateway Spike"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="incident-resolution">Action / Resolution Taken *</label>
            <textarea
              id="incident-resolution"
              data-testid="incident-resolution"
              rows={2}
              required
              placeholder="e.g. Restarted connection pool workers and purged stale redis locks"
              value={formData.resolution}
              onChange={(e) => setFormData({ ...formData, resolution: e.target.value })}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="incident-status">Current Status</label>
            <select
              id="incident-status"
              data-testid="incident-status"
              value={formData.status}
              onChange={(e) => setFormData({ ...formData, status: e.target.value })}
              className="form-input"
            >
              <option value="Resolved">Resolved (Fully Operational)</option>
              <option value="Mitigated">Mitigated (Workaround In Place)</option>
              <option value="Investigating">Investigating (Monitoring)</option>
            </select>
          </div>

          <button type="submit" data-testid="incident-submit" className="btn-primary w-full">
            Record Incident Resolution
          </button>
        </form>
      )}
    </div>
  );
}
