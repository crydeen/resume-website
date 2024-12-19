async function fetchTimelineData() {
    const response = await fetch('/web/timeline-data/');
    const data = await response.json();
    renderTimeline(data.timeline);
    renderVisualTimeline(data.timeline);
}

function renderVisualTimeline(events) {
    const timelineContainer = document.getElementById('visual-timeline');
    const svgNS = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(svgNS, "svg");
    svg.classList.add("snake-line");
    svg.setAttribute("width", "100%");
    svg.setAttribute("height", `${events.length * 150}px`);
    timelineContainer.appendChild(svg);

    // Main Striped Center Lane
    const containerWidth = timelineContainer.offsetWidth;
    const leftX = containerWidth * 0.15; // 15% from left
    const rightX = containerWidth * 0.85; // 85% from left
    const centerX = containerWidth * 0.5; // Center point

    let lastX = centerX;
    let lastY = 0;

    // Left Side of Lane
    const leftLaneLeftX = containerWidth * 0.1; // 15% from left
    const leftLaneRightX = containerWidth * 0.8; // 85% from left
    const leftLaneCenterX = containerWidth * 0.45; // Center point

    let lastLeftLaneX = leftLaneCenterX;
    let lastLeftLaneY = 0

    // Right Side of Lane
    const rightLaneLeftX = containerWidth * 0.2; // 15% from left
    const rightLaneRightX = containerWidth * 0.9; // 85% from left
    const rightLaneCenterX = containerWidth * 0.55; // Center point

    let lastRightLaneX = rightLaneCenterX;
    let lastRightLaneY = 0

    events.forEach((event, index) => {
        const direction = index % 2 === 0 ? "left" : "right";
        const currentX = direction === "left" ? leftX : rightX;
        const currentLeftLaneX = direction === "left" ? leftLaneLeftX : leftLaneRightX;
        const currentRightLaneX = direction === "left" ? rightLaneLeftX : rightLaneRightX;

        var currentY = 0
        var currentLeftLaneY = 0
        var currentRightLaneY = 0
        if (lastX == centerX) {
            currentY = index * 150 + 75;
        }
        else {
            currentY = index * 150 + 50;
        }
        currentLeftLaneY = currentY
        currentRightLaneY = currentY
        // currentLeftLaneY = direction === "left" ? currentY - 25 : currentY + 25
        // currentRightLaneY = direction === "left" ? currentY + 25 : currentY - 25
        // const currentY = index * 150 + 75;
    
        // Create path segment
        const path = document.createElementNS(svgNS, "path");
        if (lastX == centerX) {
            path.setAttribute(
            "d",
            `M${lastX} ${lastY} C${lastX} ${lastY + 75}, ${currentX} ${currentY - 75}, ${currentX} ${currentY}`
        );
        }

        else {
            path.setAttribute(
            "d",
            `M${lastX} ${lastY} C${lastX} ${lastY + 150}, ${currentX} ${currentY - 150}, ${currentX} ${currentY}`
        );
        }
        path.setAttribute("stroke", "lightgray");
        path.setAttribute("stroke-width", "4");
        path.setAttribute("fill", "none");
        path.setAttribute("stroke-dasharray","10")
        svg.appendChild(path);

        // Update last position
        lastX = currentX;
        lastY = currentY;

        // Path segment for Left Lane
        const pathLeft = document.createElementNS(svgNS, "path");
        if (lastLeftLaneX == leftLaneCenterX) {
            pathLeft.setAttribute(
            "d",
            `M${lastLeftLaneX} ${lastLeftLaneY} C${lastLeftLaneX} ${lastLeftLaneY + 50}, ${currentLeftLaneX} ${currentLeftLaneY - 100}, ${currentLeftLaneX} ${currentLeftLaneY}`
        );
        }

        else {
            if(direction == "left") {
                pathLeft.setAttribute(
            "d",
            `M${lastLeftLaneX} ${lastLeftLaneY} C${lastLeftLaneX} ${lastLeftLaneY + 125}, ${currentLeftLaneX} ${currentLeftLaneY - 175}, ${currentLeftLaneX} ${currentLeftLaneY}`
            );
            } else {
                pathLeft.setAttribute(
            "d",
            `M${lastLeftLaneX} ${lastLeftLaneY} C${lastLeftLaneX} ${lastLeftLaneY + 175}, ${currentLeftLaneX} ${currentLeftLaneY - 125}, ${currentLeftLaneX} ${currentLeftLaneY}`
            );
            }
            
        }
        pathLeft.setAttribute("stroke", "#ba8e23");
        pathLeft.setAttribute("stroke-width", "4");
        pathLeft.setAttribute("fill", "none");
        svg.appendChild(pathLeft);

        // Update last position
        lastLeftLaneX = currentLeftLaneX;
        lastLeftLaneY = currentLeftLaneY

        // Path segment for Right Lane
        const pathRight = document.createElementNS(svgNS, "path");
        if (lastRightLaneX == rightLaneCenterX) {
            pathRight.setAttribute(
            "d",
            `M${lastRightLaneX} ${lastRightLaneY} C${lastRightLaneX} ${lastRightLaneY + 100}, ${currentRightLaneX} ${currentRightLaneY - 50}, ${currentRightLaneX} ${currentRightLaneY}`
        );
        }

        else {
            if(direction=="left") {
                pathRight.setAttribute(
            "d",
            `M${lastRightLaneX} ${lastRightLaneY} C${lastRightLaneX} ${lastRightLaneY + 175}, ${currentRightLaneX} ${currentRightLaneY - 125}, ${currentRightLaneX} ${currentRightLaneY}`
            );
            } else {
                pathRight.setAttribute(
            "d",
            `M${lastRightLaneX} ${lastRightLaneY} C${lastRightLaneX} ${lastRightLaneY + 125}, ${currentRightLaneX} ${currentRightLaneY - 175}, ${currentRightLaneX} ${currentRightLaneY}`
            );
            }
        }
        pathRight.setAttribute("stroke", "#ba8e23");
        pathRight.setAttribute("stroke-width", "4");
        pathRight.setAttribute("fill", "none");
        svg.appendChild(pathRight);

        // Update last position
        lastRightLaneX = currentRightLaneX;
        lastRightLaneY = currentRightLaneY;
        
    
        // Create marker
        const marker = document.createElement("div");
        marker.className = `timeline-marker ${event.category}`;
        marker.dataset.index = index;
        marker.style.top = `${currentY}px`;
        marker.style.left = `${currentX - 6}px`; // Adjust for marker size
    
        // Marker event listeners
        marker.addEventListener("mouseenter", () => highlightMarker(index));
        marker.addEventListener("mouseleave", () => removeHighlight(index));
        marker.addEventListener("click", () => showPopup(events[index]));
    
        timelineContainer.appendChild(marker);
    
        // Create label
        const label = document.createElement("div");
        label.className = `timeline-label ${direction} ${event.category}`;
        label.style.top = `${currentY}px`;
        label.textContent = `${event.date}`;
        timelineContainer.appendChild(label);
    
        // Accomplishment linkage
        const timelineItem = document.querySelector(`.timeline-item[data-index="${index}"]`);
        if (timelineItem) {
            timelineItem.addEventListener("mouseenter", () => highlightMarker(index));
            timelineItem.addEventListener("mouseleave", () => removeHighlight(index));
        }
    });
}

function renderTimeline(events) {
    const timeline = document.getElementById('timeline');
    events.forEach((event, index) => {
        // Create the timeline item container
        const timelineItem = document.createElement('div');
        timelineItem.className = `mb-6 p-4 border-l-4 border-blue-500 bg-white shadow-md relative timeline-item ${event.category}`;
        timelineItem.innerHTML = `
            <h2 class="text-lg font-bold" data-index="${index}">${event.date}</h2>
            <h3 class="text-md font-bold">${event.title}</h3>
            <p class="text-sm">${event.description}</p>
        `;
        timelineItem.dataset.index = index;
    
        // Add hover behavior
        timelineItem.addEventListener('mouseenter', () => highlightMarker(index));
        timelineItem.addEventListener('mouseleave', () => removeHighlight(index));
    
        // Create floating info icon
        const infoIcon = document.createElement('button');
        if(event.category == "work") {
            infoIcon.className = `
            absolute top-1/2 right-4 transform -translate-y-1/2 
            bg-blue-500 text-white w-8 h-8 flex items-center justify-center 
            rounded-full shadow-lg hover:bg-blue-600 focus:outline-none
        `;
        } else {
            infoIcon.className = `
            absolute top-1/2 right-4 transform -translate-y-1/2 
            bg-green-500 text-white w-8 h-8 flex items-center justify-center 
            rounded-full shadow-lg hover:bg-green-600 focus:outline-none
        `;
        }
        
        infoIcon.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-5 h-5">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m0-4h.01M12 2a10 10 0 100 20 10 10 0 000-20z" />
            </svg>
        `;
        infoIcon.addEventListener('click', () => showPopup(events[index]));
        
        // Append info icon to the timeline item
        timelineItem.appendChild(infoIcon);
        
        // Append the timeline item to the timeline container
        timeline.appendChild(timelineItem);
    });
}


function highlightMarker(index) {
    // Highlight the marker
    document.querySelectorAll(`.timeline-marker[data-index='${index}']`).forEach(el => el.classList.add('highlight'));
    // Highlight the corresponding accomplishment
    document.querySelectorAll(`.timeline-item[data-index='${index}']`).forEach(el => el.classList.add('highlight'));
}

function removeHighlight(index) {
    // Remove highlight from the marker
    document.querySelectorAll(`.timeline-marker[data-index='${index}']`).forEach(el => el.classList.remove('highlight'));
    // Remove highlight from the corresponding accomplishment
    document.querySelectorAll(`.timeline-item[data-index='${index}']`).forEach(el => el.classList.remove('highlight'));
}


function showPopup(event) {
    document.getElementById('popup-title').textContent = event.title;
    document.getElementById('popup-description').textContent = event.details;
    document.getElementById('popup').classList.remove('hidden');
}

function closePopup() {
    document.getElementById('popup').classList.add('hidden');
}

fetchTimelineData();