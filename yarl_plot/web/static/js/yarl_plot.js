mermaid.initialize({startOnLoad:false});

transform_mermaid_div = function(elem, id) {
    var graphDefinition = elem.textContent;

    var insertSvg = function(svgCode, bindFunctions) {
        elem.innerHTML = svgCode;

        elem.style.width = elem.offsetWidth + 'px';
        elem.style.height = elem.offsetHeight + 'px';

        var svg_elem = elem.getElementsByTagName('svg')[0];
        svg_elem.style.width = elem.offsetWidth + 'px';
        svg_elem.style.height = elem.offsetHeight + 'px';

        svgPanZoom(svg_elem, {
            controlIconsEnabled: true,
            fit: 1,
            center: 1
        });
    };

    mermaid.render(id, graphDefinition, insertSvg);
};

transform_mermaid = function(classname) {
    classname = classname || 'mermaid';

    var mermaid_divs = document.getElementsByClassName(classname);

    for (var i=0; i < mermaid_divs.length; i++) {
        transform_mermaid_div(mermaid_divs[i], 'mermaid' + i);
    }
};

transform_mermaid('mermaid');
