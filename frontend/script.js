async function recommend(){
  const status=document.getElementById("status");
  const results=document.getElementById("results");
  status.textContent="Finding suitable career paths...";
  results.innerHTML="";
  const split=v=>v.split(",").map(x=>x.trim()).filter(Boolean);
  const payload={
    skills:split(document.getElementById("skills").value),
    interests:split(document.getElementById("interests").value),
    location:document.getElementById("location").value
  };
  try{
    const res=await fetch("/api/recommend",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(payload)});
    const data=await res.json();
    status.textContent="";
    results.innerHTML="<h2>Recommended Career Paths</h2>"+data.recommendations.map(r=>`
      <div class="result">
        <div class="top"><h3>${r.role}</h3><div class="score">${r.score}% Match</div></div>
        <div class="bar"><div class="fill" style="width:${r.score}%"></div></div>
        <p class="muted"><b>Matched skills:</b> ${r.matchedSkills.length?r.matchedSkills.join(", "):"None yet"}</p>
        <div class="chips missing"><b>Skills to learn:</b> ${r.missingSkills.map(s=>`<span>${s}</span>`).join("")}</div>
      </div>`).join("");
  }catch(e){status.textContent="Please start the Flask backend and try again."}
}
