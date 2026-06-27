/**
 * App.jsx
 * -------
 * Root application component for IntergalacticCargoTriager.
 *
 * Responsibilities:
 *  - Fetch cargo data from the Flask backend (GET /api/cargo).
 *  - Pass data down to CargoTable for sorted display.
 *  - Expose a "Sync Data" button that triggers a re-fetch with the
 *    exact 2.5-second animation defined in the assignment spec.
 *  - Render the animated starfield background, header, stats pills, and footer.
 */

import React, { useState, useEffect, useCallback } from 'react';
import CargoTable from './components/CargoTable';
import SyncButton from './components/SyncButton';
import StatusBar  from './components/StatusBar';

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

const API_URL = '/api/cargo';

// ---------------------------------------------------------------------------
// Stats helpers
// ---------------------------------------------------------------------------

const computeStats = (records) => ({
  total:   records.length,
  earth:   records.filter((r) => r.destination === 'Earth').length,
  sector7: records.filter((r) => r.sector7_applied).length,
});

// ---------------------------------------------------------------------------
// App component
// ---------------------------------------------------------------------------

const App = () => {
  const [records, setRecords]     = useState([]);
  const [loading, setLoading]     = useState(true);
  const [error,   setError]       = useState(null);

  // Fetch data from the backend
  const fetchCargo = useCallback(async () => {
    setError(null);
    try {
      const response = await fetch(API_URL);

      if (!response.ok) {
        throw new Error(
          `Server responded with ${response.status}: ${response.statusText}`
        );
      }

      const data = await response.json();

      if (!Array.isArray(data)) {
        throw new Error('Unexpected response format from server.');
      }

      setRecords(data);
    } catch (err) {
      setError(
        err.message ||
          'Failed to connect to cargo control. Make sure the backend is running.'
      );
    }
  }, []);

  // Initial load
  useEffect(() => {
    (async () => {
      setLoading(true);
      await fetchCargo();
      setLoading(false);
    })();
  }, [fetchCargo]);

  const stats = computeStats(records);

  // ---------------------------------------------------------------------------
  // Render
  // ---------------------------------------------------------------------------

  return (
    <>
      {/* Animated starfield background */}
      <div className="starfield" aria-hidden="true" />

      <main className="app-layout">
        {/* Header */}
        <header className="app-header">
          <div className="header-badge">
            <span className="dot" />
            <span>Live Feed — Intergalactic Cargo Control</span>
          </div>
          <h1 className="header-title">Intergalactic Cargo Triager</h1>
          <p className="header-subtitle">
            Real-time manifest intelligence across the known universe.
          </p>
        </header>

        {/* Controls bar */}
        <div className="controls-bar">
          {/* Stats pills */}
          <div className="stats-pills" aria-label="Cargo statistics">
            <span className="stat-pill total" aria-label={`Total records: ${stats.total}`}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                strokeLinejoin="round" aria-hidden="true">
                <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/>
              </svg>
              {stats.total} records
            </span>

            <span className="stat-pill earth" aria-label={`Earth destinations: ${stats.earth}`}>
              🌍 {stats.earth} Earth
            </span>

            <span className="stat-pill sector7" aria-label={`Sector 7 shipments: ${stats.sector7}`}>
              ⚡ {stats.sector7} Sector-7
            </span>
          </div>

          {/* Sync button */}
          <SyncButton onSync={fetchCargo} />
        </div>

        {/* Loading / Error status */}
        <StatusBar loading={loading} error={error} />

        {/* Cargo data table */}
        {!loading && !error && (
          <CargoTable records={records} />
        )}

        {/* Footer */}
        <footer className="app-footer">
          <p>IntergalacticCargoTriager-Lohith &nbsp;&middot;&nbsp; 2026 &nbsp;&middot;&nbsp; Flask + React + Vite</p>
        </footer>
      </main>
    </>
  );
};

export default App;
