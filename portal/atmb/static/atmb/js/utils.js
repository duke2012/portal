function getMenu(parentId, data) {
    return data.filter(function (node) {
        return ( node.parent_id === parentId );
    }).sort(function (a, b) {
        return a.order_no - b.order_no
    }).map(function (node) {
        var exists = data.some(function (childNode) {
            return childNode.parent_id === node.id;
        });
        var subMenu = (exists) ? '<ul>' + getMenu(node.id, data).join('') + '</ul>' : "";
        return '<li   value=' + node.id + '>' + node.name + subMenu + '</li>';
    });
}