"use strict";

const vscode = require("vscode");

function onCommand() {
  let editor = vscode.window.activeTextEditor;
  if (!editor) {
    return;
  }

  let document = editor.document;
  let position = editor.selection.active;
  let wordRange = document.getWordRangeAtPosition(position);

  if (wordRange) {
    let word = document.getText(wordRange);
    let toggledWord = toggleCase(word);

    editor.edit(function (editBuilder) {
      editBuilder.replace(wordRange, toggledWord);
    });
  }
}

function toggleCase(text) {
  if (/_/.test(text)) {
    return toCamelCase(text);
  } else {
    return toSnakeCase(text);
  }
}

function toCamelCase(text) {
  const words = text.split(/_+/);
  const Words = words.map(upFirstLetter);

  return [words[0], ...Words.slice(1)].join("");
}

function upFirstLetter(text) {
  if (text.length === 0) {
    return text;
  }
  return text[0].toUpperCase() + text.slice(1);
}

function toSnakeCase(text) {
  return text
    .replace(/[A-ZА-ЯЁ]/g, (letter) => "_" + letter.toLowerCase())
    .replace(/^_/, "");
}

exports.activate = function activate(context) {
  let disposable = vscode.commands.registerCommand(
    "toggle-snake-camel-case.ToggleSnakeCamelCase",
    onCommand
  );
  context.subscriptions.push(disposable);
};

exports.deactivate = function () {};
