/**
 * Header Component
 * Page header with title and breadcrumb navigation
 */

import React from 'react';

/**
 * Header Component
 * @param {Object} props - Component props
 * @param {string} props.title - Page title
 * @param {string} props.breadcrumb - Breadcrumb text
 */
function Header({ title, breadcrumb }) {
  return (
    <div className="page-header">
      <h1 className="page-title">{title}</h1>
      <div className="breadcrumb">
        HireIQ <span>/</span> {breadcrumb}
      </div>
    </div>
  );
}

export default Header;
