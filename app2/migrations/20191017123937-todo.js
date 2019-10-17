module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable("Todo", {
      todo_id: {
        allowNull: false,
        primaryKey: true,
        type: Sequelize.UUID,
        defaultValue: Sequelize.UUIDV4,
      },
      text: {
        type: Sequelize.STRING,
      },
      title: {
        type: Sequelize.STRING,
      },
      user_id: {
        type: Sequelize.UUID,
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
        defaultValue: Date.now(),
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
        defaultValue: Date.now(),
      },
    });
  },

  down: queryInterface => {
    return queryInterface.dropTable("Todo");
  },
};
