/**
 * StatusBar.jsx
 * -------------
 * Displays a loading spinner or error message while data is being fetched.
 *
 * Props:
 *  loading  – boolean  – show loading state
 *  error    – string   – error message (null/undefined = no error)
 */

import React from 'react';

const StatusBar = ({ loading, error }) => {
  if (loading) {
    return (
      <div className="status-banner loading" role="status" aria-live="polite">
        <div className="spinner" aria-hidden="true" />
        <span>Establishing quantum link with cargo control...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="status-banner error" role="alert" aria-live="assertive">
        <svg
          aria-hidden="true"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          style={{ flexShrink: 0 }}
        >
          <circle cx="12" cy="12" r="10" />
          <line x1="12" y1="8" x2="12" y2="12" />
          <line x1="12" y1="16" x2="12.01" y2="16" />
        </svg>
        <span>{error}</span>
      </div>
    );
  }

  return null;
};

export default StatusBar;
