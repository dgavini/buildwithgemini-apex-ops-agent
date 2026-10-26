import React, { useState } from 'react';
import { History, CheckCircle, Clock, Trash2, Filter } from 'lucide-react';

export default function ActivityLog({ activities, onClear }) {
  const [filter, setFilter] = useState('ALL');

  const filtered = activities.filter((act) => {
    if (filter === 'ALL') return true;
    return act.type.toLowerCase().includes(filter.toLowerCase());
  });

  const getTypeBadge = (type) => {
    if (type.includes('Onboarding')) return 'badge-blue';
    if (type.includes('Expense')) return 'badge-emerald';
    return 'badge-rose';
  };

  return (
    <div className="activity-container" data-testid="activity-feed">
      <div className="activity-header">
        <div className="flex items-center gap-2">
          <History size={20} className="text-gray-600" />
          <h3 className="font-bold text-gray-800 text-base">Live Activity & Task Audit Log</h3>
          <span className="bg-gray-100 text-gray-700 px-2 py-0.5 rounded-full text-xs font-semibold">
            {activities.length} total
          </span>
        </div>

        <div className="flex items-center gap-2">
          <div className="flex bg-gray-100 p-0.5 rounded-lg text-xs font-medium">
            <button
              onClick={() => setFilter('ALL')}
              className={`px-2.5 py-1 rounded-md transition ${
                filter === 'ALL' ? 'bg-white shadow-sm text-gray-900' : 'text-gray-500'
              }`}
            >
              All
            </button>
            <button
              onClick={() => setFilter('Onboarding')}
              className={`px-2.5 py-1 rounded-md transition ${
                filter === 'Onboarding' ? 'bg-white shadow-sm text-blue-700' : 'text-gray-500'
              }`}
            >
              Onboarding
            </button>
            <button
              onClick={() => setFilter('Expense')}
              className={`px-2.5 py-1 rounded-md transition ${
                filter === 'Expense' ? 'bg-white shadow-sm text-emerald-700' : 'text-gray-500'
              }`}
            >
              Expenses
            </button>
            <button
              onClick={() => setFilter('Incident')}
              className={`px-2.5 py-1 rounded-md transition ${
                filter === 'Incident' ? 'bg-white shadow-sm text-rose-700' : 'text-gray-500'
              }`}
            >
              Incidents
            </button>
          </div>

          {activities.length > 0 && (
            <button
              onClick={onClear}
              className="text-gray-400 hover:text-rose-600 p-1 rounded transition"
              title="Clear Log"
            >
              <Trash2 size={16} />
            </button>
          )}
        </div>
      </div>

      {filtered.length === 0 ? (
        <div className="text-center py-8 text-gray-400 text-sm">
          No task activity recorded yet. Run a task above to see live updates.
        </div>
      ) : (
        <div className="activity-list">
          {filtered.map((item, index) => (
            <div
              key={item.id + index}
              data-testid="activity-item"
              className="activity-item"
            >
              <div className="flex justify-between items-start mb-1">
                <div className="flex items-center gap-2">
                  <span className={`type-badge ${getTypeBadge(item.type)}`}>
                    {item.type}
                  </span>
                  <span className="font-mono text-xs font-bold text-gray-600">
                    {item.id}
                  </span>
                </div>
                <span className="text-xs text-gray-400 flex items-center gap-1">
                  <Clock size={12} /> {item.timestamp}
                </span>
              </div>
              <h4 className="font-semibold text-gray-900 text-sm mb-0.5">{item.title}</h4>
              <p className="text-xs text-gray-600">{item.details}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
