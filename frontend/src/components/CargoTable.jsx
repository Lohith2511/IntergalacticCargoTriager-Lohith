/**
 * CargoTable.jsx
 * ---------------
 * Renders the sorted cargo records in a responsive table.
 *
 * Sorting rules (per spec):
 *  - Primary : Sort by final_weight descending (heaviest first).
 *  - Exception: Any cargo with destination "Earth" is always placed at the
 *               bottom, regardless of its weight.
 *
 * Props:
 *  records  – array of cargo record objects from the API.
 */

import React, { useMemo } from 'react';

// ---------------------------------------------------------------------------
// Destination emoji helper
// ---------------------------------------------------------------------------

const DEST_ICONS = {
  'Mars':     '🔴',
  'Lunar':    '🌙',
  'Titan':    '🪐',
  'Venus':    '☁️',
  'Sector-7': '⚡',
  'Europa':   '❄️',
  'Asteroid': '☄️',
  'Earth':    '🌍',
  'Jupiter':  '🟠',
  'Pluto':    '🔵',
  'Neptune':  '🌊',
};

const getDestIcon = (destination) => {
  for (const [key, icon] of Object.entries(DEST_ICONS)) {
    if (destination.includes(key)) return icon;
  }
  return '🛸';
};

// ---------------------------------------------------------------------------
// Sort helper
// ---------------------------------------------------------------------------

/**
 * Sort cargo records:
 *  1. Earth destinations always sink to the bottom.
 *  2. Within each group, sort by final_weight descending.
 */
const sortCargo = (records) => {
  return [...records].sort((a, b) => {
    const aIsEarth = a.destination === 'Earth';
    const bIsEarth = b.destination === 'Earth';

    // Earth always last
    if (aIsEarth && !bIsEarth) return 1;
    if (!aIsEarth && bIsEarth) return -1;

    // Both Earth (edge case): keep stable order
    if (aIsEarth && bIsEarth) return 0;

    // Neither Earth: sort by weight descending
    return b.final_weight - a.final_weight;
  });
};

// ---------------------------------------------------------------------------
// Component
// ---------------------------------------------------------------------------

const CargoTable = ({ records }) => {
  const sorted = useMemo(() => sortCargo(records), [records]);

  // Find max weight (excluding Earth rows) for the weight bar scale
  const maxWeight = useMemo(() => {
    const nonEarth = sorted.filter((r) => r.destination !== 'Earth');
    return nonEarth.length > 0 ? Math.max(...nonEarth.map((r) => r.final_weight)) : 1;
  }, [sorted]);

  if (!sorted || sorted.length === 0) {
    return (
      <div className="no-data">
        <div className="no-data-icon">🛸</div>
        <p className="no-data-text">No cargo records found.</p>
      </div>
    );
  }

  return (
    <div className="table-wrapper">
      <table className="cargo-table" aria-label="Intergalactic Cargo Manifest">
        <thead>
          <tr>
            <th aria-label="Rank">#</th>
            <th>Cargo ID</th>
            <th>Destination</th>
            <th>Weight</th>
            <th>Distribution</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((record, index) => {
            const isEarth = record.destination === 'Earth';
            const isSector7 = record.sector7_applied;
            const barWidth = isEarth
              ? (record.final_weight / maxWeight) * 100
              : (record.final_weight / maxWeight) * 100;

            return (
              <tr
                key={record.cargo_id}
                className={isEarth ? 'earth-row' : ''}
                style={{ animationDelay: `${index * 45}ms` }}
              >
                {/* Rank */}
                <td className="rank-cell">{index + 1}</td>

                {/* Cargo ID */}
                <td>
                  <span className="cargo-id-badge">{record.cargo_id}</span>
                </td>

                {/* Destination */}
                <td>
                  <div className="destination-cell">
                    <span className="destination-icon" aria-hidden="true">
                      {getDestIcon(record.destination)}
                    </span>
                    <span>{record.destination}</span>
                    {isEarth   && <span className="earth-tag">Home</span>}
                    {isSector7 && <span className="sector7-tag">×1.45</span>}
                  </div>
                </td>

                {/* Weight */}
                <td>
                  <span className="weight-cell">
                    <span className="weight-value">{record.final_weight.toLocaleString()}</span>
                    <span className="weight-unit"> kg</span>
                  </span>
                </td>

                {/* Weight distribution bar */}
                <td>
                  <div className="weight-bar-container" aria-hidden="true">
                    <div
                      className="weight-bar"
                      style={{ width: `${Math.min(barWidth, 100)}%` }}
                    />
                  </div>
                </td>

                {/* Date */}
                <td className="date-cell">{record.date}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default CargoTable;
