#!/usr/bin/node
exports.nbOccurences = function (list, seaelement) {
	return list.filter(y => y === seaelement).length;
};
