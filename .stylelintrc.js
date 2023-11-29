module.exports = {
  extends: [
    "stylelint-config-standard",
    "stylelint-config-recess-order",
    "stylelint-config-prettier",
  ],
  rules: {
    "selector-id-pattern": "^[a-z][a-zA-Z0-9]+$",
    "selector-class-pattern": "^[a-z][a-zA-Z0-9]+$",
  },
};
