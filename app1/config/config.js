module.exports = {
  development: {
    dialect: "sqlite",
    storage: "user.db",
    logging: false,
  },
  production: {
    dialect: "sqlite",
    storage: "todo.db",
    logging: false,
  },
};
