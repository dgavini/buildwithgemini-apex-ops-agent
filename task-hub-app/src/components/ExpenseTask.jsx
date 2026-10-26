import React, { useState } from 'react';
import { Receipt, CheckCircle2, AlertCircle, DollarSign } from 'lucide-react';

export default function ExpenseTask({ onComplete }) {
  const [formData, setFormData] = useState({
    category: 'Software & Tools',
    merchant: '',
    amount: '',
    notes: '',
    urgency: 'Standard',
  });

  const [submittedData, setSubmittedData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const numAmount = parseFloat(formData.amount);
    if (!formData.merchant || isNaN(numAmount) || numAmount <= 0) return;

    const claimId = `EXP-${Math.floor(1000 + Math.random() * 9000)}`;
    const isAutoApproved = numAmount <= 500;
    const approvalStatus = isAutoApproved ? 'Auto-Approved' : 'Requires Manager Review';

    const completedRecord = {
      id: claimId,
      type: 'Expense Claim',
      title: `$${numAmount.toFixed(2)} - ${formData.merchant}`,
      details: `${formData.category} • ${approvalStatus} • ${formData.urgency} priority`,
      timestamp: new Date().toLocaleTimeString(),
      status: isAutoApproved ? 'Approved' : 'Pending',
      metadata: {
        ...formData,
        amount: numAmount.toFixed(2),
        claimId,
        isAutoApproved,
        approvalStatus,
      },
    };

    setSubmittedData(completedRecord);
    if (onComplete) onComplete(completedRecord);
  };

  const handleReset = () => {
    setSubmittedData(null);
    setFormData({
      category: 'Software & Tools',
      merchant: '',
      amount: '',
      notes: '',
      urgency: 'Standard',
    });
  };

  return (
    <div className="task-card">
      <div className="task-header">
        <div className="task-icon-wrapper bg-emerald-100 text-emerald-600">
          <Receipt size={24} />
        </div>
        <div>
          <h2 className="task-title">Task 2: Expense Claim Submission</h2>
          <p className="task-subtitle">Submit corporate expenses with automatic financial policy evaluation</p>
        </div>
      </div>

      {submittedData ? (
        <div
          className={`result-box ${
            submittedData.metadata.isAutoApproved
              ? 'border-emerald-200 bg-emerald-50/50'
              : 'border-amber-200 bg-amber-50/50'
          }`}
          data-testid="expense-success-card"
        >
          <div
            className={`flex items-center gap-2 font-semibold mb-3 ${
              submittedData.metadata.isAutoApproved ? 'text-emerald-700' : 'text-amber-800'
            }`}
          >
            {submittedData.metadata.isAutoApproved ? (
              <CheckCircle2 size={20} />
            ) : (
              <AlertCircle size={20} />
            )}
            <span>Claim Filed: {submittedData.metadata.approvalStatus}</span>
          </div>

          <div className="receipt-card">
            <div className="flex justify-between items-center mb-2">
              <span className="text-xs uppercase font-semibold text-gray-500">
                {submittedData.metadata.category}
              </span>
              <span className="font-mono text-sm font-bold text-gray-700">
                {submittedData.id}
              </span>
            </div>
            <div className="text-2xl font-bold text-gray-900 mb-1">
              ${submittedData.metadata.amount}
            </div>
            <div className="text-sm text-gray-600 font-medium mb-3">
              Merchant: {submittedData.metadata.merchant}
            </div>
            {submittedData.metadata.notes && (
              <div className="text-xs text-gray-500 bg-gray-50 p-2 rounded border border-gray-200 mb-3">
                "{submittedData.metadata.notes}"
              </div>
            )}
            <div className="text-xs text-gray-500 pt-2 border-t border-gray-200 flex justify-between">
              <span>Policy Rule: Threshold $500</span>
              <span className="font-semibold text-gray-700">{submittedData.metadata.urgency}</span>
            </div>
          </div>

          <button onClick={handleReset} className="btn-secondary mt-4 w-full">
            Submit Another Expense
          </button>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="task-form">
          <div className="grid-2">
            <div className="form-group">
              <label htmlFor="expense-category">Category</label>
              <select
                id="expense-category"
                data-testid="expense-category"
                value={formData.category}
                onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                className="form-input"
              >
                <option value="Software & Tools">Software & Cloud Services</option>
                <option value="Travel & Lodging">Travel & Lodging</option>
                <option value="Client Meals">Client Meals & Dining</option>
                <option value="Office Equipment">Office & Hardware Equipment</option>
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="expense-merchant">Merchant / Vendor *</label>
              <input
                id="expense-merchant"
                data-testid="expense-merchant"
                type="text"
                required
                placeholder="e.g. AWS Cloud Services"
                value={formData.merchant}
                onChange={(e) => setFormData({ ...formData, merchant: e.target.value })}
                className="form-input"
              />
            </div>
          </div>

          <div className="grid-2">
            <div className="form-group">
              <label htmlFor="expense-amount">Amount (USD) *</label>
              <div className="input-with-icon">
                <DollarSign size={16} className="input-icon" />
                <input
                  id="expense-amount"
                  data-testid="expense-amount"
                  type="number"
                  step="0.01"
                  min="0.01"
                  required
                  placeholder="0.00"
                  value={formData.amount}
                  onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
                  className="form-input pl-8"
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="expense-urgency">Urgency</label>
              <select
                id="expense-urgency"
                data-testid="expense-urgency"
                value={formData.urgency}
                onChange={(e) => setFormData({ ...formData, urgency: e.target.value })}
                className="form-input"
              >
                <option value="Standard">Standard (Regular Payroll)</option>
                <option value="Urgent">Urgent (Express 24h Reimbursement)</option>
              </select>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="expense-notes">Business Justification / Purpose</label>
            <textarea
              id="expense-notes"
              data-testid="expense-notes"
              rows={2}
              placeholder="e.g. Monthly hosting infrastructure for analytics pipeline"
              value={formData.notes}
              onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
              className="form-input"
            />
          </div>

          <button type="submit" data-testid="expense-submit" className="btn-primary w-full">
            Submit Expense Claim
          </button>
        </form>
      )}
    </div>
  );
}
