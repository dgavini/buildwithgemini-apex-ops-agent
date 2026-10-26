import React, { useState } from 'react';
import { UserPlus, CheckCircle2, ShieldCheck, Laptop } from 'lucide-react';

export default function OnboardingTask({ onComplete }) {
  const [formData, setFormData] = useState({
    name: '',
    dept: 'Engineering',
    email: '',
    equipLaptop: true,
    equipMonitor: false,
    equipHeadset: false,
    startDate: new Date().toISOString().split('T')[0],
  });

  const [submittedData, setSubmittedData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.name || !formData.email) return;

    const empId = `EMP-${Math.floor(1000 + Math.random() * 9000)}`;
    const equipmentList = [
      formData.equipLaptop && 'MacBook Pro 16"',
      formData.equipMonitor && '4K UltraFine Monitor',
      formData.equipHeadset && 'Noise-Cancelling Headset',
    ].filter(Boolean);

    const completedRecord = {
      id: empId,
      type: 'Onboarding',
      title: `Onboarded ${formData.name}`,
      details: `${formData.dept} • ${formData.email} • Equipment: ${equipmentList.join(', ') || 'Standard Kit'}`,
      timestamp: new Date().toLocaleTimeString(),
      status: 'Active',
      metadata: { ...formData, empId, equipmentList },
    };

    setSubmittedData(completedRecord);
    if (onComplete) onComplete(completedRecord);
  };

  const handleReset = () => {
    setSubmittedData(null);
    setFormData({
      name: '',
      dept: 'Engineering',
      email: '',
      equipLaptop: true,
      equipMonitor: false,
      equipHeadset: false,
      startDate: new Date().toISOString().split('T')[0],
    });
  };

  return (
    <div className="task-card">
      <div className="task-header">
        <div className="task-icon-wrapper bg-blue-100 text-blue-600">
          <UserPlus size={24} />
        </div>
        <div>
          <h2 className="task-title">Task 1: Employee Onboarding</h2>
          <p className="task-subtitle">Provision employee identity, workspace roles, and hardware gear</p>
        </div>
      </div>

      {submittedData ? (
        <div className="result-box border-blue-200 bg-blue-50/50" data-testid="onboard-success-card">
          <div className="flex items-center gap-2 text-blue-700 font-semibold mb-3">
            <CheckCircle2 size={20} />
            <span>Onboarding Completed Successfully</span>
          </div>

          <div className="badge-card">
            <div className="badge-header">
              <span className="badge-tag">{submittedData.metadata.dept}</span>
              <span className="badge-id font-mono font-bold">{submittedData.id}</span>
            </div>
            <h3 className="badge-name">{submittedData.metadata.name}</h3>
            <p className="text-sm text-gray-500">{submittedData.metadata.email}</p>
            <div className="mt-4 pt-3 border-t border-gray-200 text-xs text-gray-600 flex flex-wrap gap-2">
              <span className="font-semibold">Gear:</span>
              {submittedData.metadata.equipmentList.map((eq, i) => (
                <span key={i} className="bg-white px-2 py-0.5 rounded border border-gray-200">
                  {eq}
                </span>
              ))}
            </div>
          </div>

          <button onClick={handleReset} className="btn-secondary mt-4 w-full">
            Onboard Another Employee
          </button>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="task-form">
          <div className="form-group">
            <label htmlFor="onboard-name">Full Name *</label>
            <input
              id="onboard-name"
              data-testid="onboard-name"
              type="text"
              required
              placeholder="e.g. Sarah Jenkins"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className="form-input"
            />
          </div>

          <div className="grid-2">
            <div className="form-group">
              <label htmlFor="onboard-dept">Department</label>
              <select
                id="onboard-dept"
                data-testid="onboard-dept"
                value={formData.dept}
                onChange={(e) => setFormData({ ...formData, dept: e.target.value })}
                className="form-input"
              >
                <option value="Engineering">Engineering</option>
                <option value="Product">Product & Design</option>
                <option value="Marketing">Marketing</option>
                <option value="Sales">Sales & Revenue</option>
                <option value="Security">Security & IT</option>
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="onboard-email">Work Email *</label>
              <input
                id="onboard-email"
                data-testid="onboard-email"
                type="email"
                required
                placeholder="s.jenkins@company.com"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                className="form-input"
              />
            </div>
          </div>

          <div className="form-group">
            <label>Hardware Equipment Needed</label>
            <div className="checkbox-group">
              <label className="checkbox-label">
                <input
                  type="checkbox"
                  data-testid="onboard-equip-laptop"
                  checked={formData.equipLaptop}
                  onChange={(e) => setFormData({ ...formData, equipLaptop: e.target.checked })}
                />
                <span>Laptop (16" Pro)</span>
              </label>

              <label className="checkbox-label">
                <input
                  type="checkbox"
                  data-testid="onboard-equip-monitor"
                  checked={formData.equipMonitor}
                  onChange={(e) => setFormData({ ...formData, equipMonitor: e.target.checked })}
                />
                <span>4K External Monitor</span>
              </label>

              <label className="checkbox-label">
                <input
                  type="checkbox"
                  data-testid="onboard-equip-headset"
                  checked={formData.equipHeadset}
                  onChange={(e) => setFormData({ ...formData, equipHeadset: e.target.checked })}
                />
                <span>ANC Headset</span>
              </label>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="onboard-date">Start Date</label>
            <input
              id="onboard-date"
              data-testid="onboard-date"
              type="date"
              value={formData.startDate}
              onChange={(e) => setFormData({ ...formData, startDate: e.target.value })}
              className="form-input"
            />
          </div>

          <button type="submit" data-testid="onboard-submit" className="btn-primary w-full">
            Submit Employee Onboarding
          </button>
        </form>
      )}
    </div>
  );
}
