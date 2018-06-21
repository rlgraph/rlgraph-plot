mermaidAPI.initialize({startOnLoad:true});

transform_mermaid_div = function(elem, id) {
    var graphDefinition = elem.textContent;

    var insertSvg = function(svgCode, bindFunctions) {
        elem.innerHTML = svgCode;
    };

    mermaidAPI.render(id, graphDefinition, insertSvg)
};

transform_mermaid = function(classname) {
    classname = classname || 'mermaid';

    var mermaid_divs = document.getElementsByClassName(classname);

    for (var i=0; i < mermaid_divs.length; i++) {
        transform_mermaid_div(mermaid_divs[i], 'mermaid' + i);
    }
};

transform_mermaid('mermaid');