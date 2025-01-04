class GraphQLQueries:
    @staticmethod
    def get_board_details(board_id: str) -> str:
        """
        Retrieves the groups of a specified board.

        Args:
            board_id (str): board id where the group is located

        Returns: 
            dict: response data containing the groups id,name
        """
        return f"""
        {{
            boards (ids: {board_id}) {{
                id
                name
                groups {{
                    id
                    title
                }}
            }}
        }}
        """