def get_attachment_image(model, res_id, name, env):
    """
    Fungsi untuk mendapatkan ID attachment berdasarkan model, res_id, dan nama.
    :param model: Model yang terkait dengan attachment
    :param res_id: ID record yang terkait
    :param name: Nama file attachment
    :param env: Environment Odoo untuk mengakses database
    :return: ID attachment jika ditemukan, atau None jika tidak ada
    """
    env.cr.execute("""
        SELECT id FROM ir_attachment
        WHERE res_model = %s 
        AND res_id = %s 
        AND name = %s
        LIMIT 1
    """, (model, res_id, name))

    attachment_image = env.cr.fetchone()
    
    if attachment_image:
        return attachment_image[0]
    return None
