import { fetchData } from '../../js/laws.js';

document.addEventListener('DOMContentLoaded', e => {
  fetchData('Vizcarra.json', 'justicia')
});
