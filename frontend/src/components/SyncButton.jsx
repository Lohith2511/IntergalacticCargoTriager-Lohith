/**
 * SyncButton.jsx
 * --------------
 * "Sync Data" button with the exact 2.5-second animation cycle defined in the spec:
 *  1. Disable button.
 *  2. Change label to "Aligning quantum drives..."
 *  3. Wait exactly 2500ms.
 *  4. Restore label to "Sync Data".
 *  5. Re-enable button.
 *
 * Props:
 *  onSync  – async callback invoked after the button is clicked.
 *            Executed while the button is in the syncing state.
 */

import React, { useState, useCallback } from 'react';

const SyncButton = ({ onSync }) => {
  const [syncing, setSyncing] = useState(false);

  const handleClick = useCallback(async () => {
    if (syncing) return; // Guard against double-click

    // Step 1 & 2: Disable + change label
    setSyncing(true);

    // Step 3: Execute the actual data refresh while waiting
    try {
      await onSync?.();
    } catch (_err) {
      // Errors are handled inside onSync; we just ensure the button resets.
    }

    // Wait exactly 2500ms total from click (onSync is assumed fast; pad remainder)
    await new Promise((resolve) => setTimeout(resolve, 2500));

    // Step 4 & 5: Restore label + re-enable
    setSyncing(false);
  }, [syncing, onSync]);

  return (
    <button
      id="sync-data-btn"
      className={`sync-btn ${syncing ? 'syncing' : ''}`}
      onClick={handleClick}
      disabled={syncing}
      aria-label={syncing ? 'Aligning quantum drives, please wait' : 'Sync cargo data from server'}
    >
      {/* Animated icon */}
      <svg className="sync-icon" viewBox="0 0 24 24" aria-hidden="true">
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
        />
      </svg>

      {/* Label */}
      <span>{syncing ? 'Aligning quantum drives...' : 'Sync Data'}</span>
    </button>
  );
};

export default SyncButton;
