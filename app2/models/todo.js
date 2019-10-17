module.exports = (sequelize, Sequelize) => {
  const todoSchema = {
    todo_id: {
      type: Sequelize.UUID,
      primaryKey: true,
      unique: true,
      allowNull: false,
      defaultValue: Sequelize.UUIDV4,
    },
    text: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    title: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    user_id: {
      type: Sequelize.UUID,
      allowNull: false,
    },
  };

  const todo = sequelize.define("Todo", todoSchema, {});
  return todo;
};
