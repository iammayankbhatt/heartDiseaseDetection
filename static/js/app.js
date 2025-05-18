// Client‑side range validation (extra layer in addition to HTML attributes)
document.getElementById('predictForm').addEventListener('submit', function (e) {
  const ranges = {
    age: [18, 120],
    sex: [0, 1],
    cp: [0, 3],
    trestbps: [70, 250],
    chol: [100, 600],
    fbs: [0, 1],
    restecg: [0, 2],
    thalach: [60, 250],
    exang: [0, 1],
    oldpeak: [0, 10],
    slope: [0, 2],
    ca: [0, 3],
    thal: [1, 3]
  };

  for (const [id, [min, max]] of Object.entries(ranges)) {
    const el = document.getElementById(id);
    const val = parseFloat(el.value);
    if (isNaN(val) || val < min || val > max) {
      alert(`${el.previousElementSibling.textContent} must be between ${min} and ${max}.`);
      el.focus();
      e.preventDefault();
      return;
    }
  }
});