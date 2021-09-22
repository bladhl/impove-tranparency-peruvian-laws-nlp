

// document.addEventListener('DOMContentLoaded', e => { fetchData('MMerino_period.json', 'agricultura') });

// get laws
export const fetchData = async (path, topic) => {
  const res = await fetch(`../../../json/${path}`);
  const data = await res.json()
  console.log(data)
  drawLaws(data, topic)
}

const drawLaws = (data, topic) => {
  const templateLaw = document.getElementById('template-law').content;
  const lawCard = document.getElementById('law-card');
  const fragment = document.createDocumentFragment();

  Object.entries(data).forEach(([key, element]) => {
    if (element.topico == topic) {
      templateLaw.getElementById('law').textContent = element.objeto
      const clone = templateLaw.cloneNode(true)
      fragment.appendChild(clone)
    }
  });
  lawCard.appendChild(fragment);
}