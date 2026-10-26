import React, { useState } from 'react';
import { UserPlus, Receipt, AlertOctagon, Activity, Sparkles, CheckCircle } from 'lucide-react';
import OnboardingTask from './components/OnboardingTask';
import ExpenseTask from './components/ExpenseTask';
import IncidentTask from './components/IncidentTask';
import ActivityLog from './components/ActivityLog';

export default function App() {
  const [activeTab, setActiveTab] = useState('onboarding');
  const [activities, setActivities] = useState([
    {
      id: 'EMP-4012',
      type: 'Onboarding',
      title: 'Onboarded Alex Rivera',
      details: 'Product & Design • a.rivera@company.com • Equipment: MacBook Pro 16", 4K UltraFine Monitor',
      timestamp: '10:14 AM',
      status: 'Active',
    },
    {
      id: 'EXP-8841',
      type: 'Expense Claim',
      title: '$149.00 - JetBrains All Products Pack',
      details: 'Software & Tools • Auto-Approved • Standard priority',
      timestamp: '11:02 AM',
      status: 'Approved',
    },
  ]);

  const handleTaskComplete = (newRecord) => {
    setActivities((prev) => [newRecord, ...prev]);
  };

  const handleClearActivities = () => {
    setActivities([]);
  };

  return (
    <div className="app-shell">
      {/* Top Navbar */}
      <header className="navbar">
        <div className="navbar-container">
          <div className="brand-group">
            <div className="brand-icon">
              <Activity size={22} className="text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="brand-title">Apex Operations Hub</h1>
                <span className="badge-pill">Local App</span>
              </div>
              <p className="brand-sub">Multi-Task Agent Execution & Workflow Portal</p>
            </div>
          </div>

          <div className="system-status">
            <span className="status-dot"></span>
            <span className="text-xs font-semibold text-gray-700">UI & Automation Ready</span>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="main-content">
        {/* Navigation Tabs */}
        <div className="tab-bar">
          <button
            data-testid="tab-onboarding"
            onClick={() => setActiveTab('onboarding')}
            className={`tab-btn ${activeTab === 'onboarding' ? 'tab-active-blue' : ''}`}
          >
            <UserPlus size={18} />
            <span>1. Employee Onboarding</span>
          </button>

          <button
            data-testid="tab-expenses"
            onClick={() => setActiveTab('expenses')}
            className={`tab-btn ${activeTab === 'expenses' ? 'tab-active-emerald' : ''}`}
          >
            <Receipt size={18} />
            <span>2. Expense Claims</span>
          </button>

          <button
            data-testid="tab-incidents"
            onClick={() => setActiveTab('incidents')}
            className={`tab-btn ${activeTab === 'incidents' ? 'tab-active-rose' : ''}`}
          >
            <AlertOctagon size={18} />
            <span>3. Incident Triage</span>
          </button>
        </div>

        {/* Task Form Panes */}
        <div className="task-panel">
          {activeTab === 'onboarding' && <OnboardingTask onComplete={handleTaskComplete} />}
          {activeTab === 'expenses' && <ExpenseTask onComplete={handleTaskComplete} />}
          {activeTab === 'incidents' && <IncidentTask onComplete={handleTaskComplete} />}
        </div>

        {/* Bottom Activity & Audit Log */}
        <ActivityLog activities={activities} onClear={handleClearActivities} />
      </main>

      <footer className="footer">
        <p>Apex Operations Hub · Built for AI Agent Task Automation & Human Workflows</p>
      </footer>
    </div>
  );
}
