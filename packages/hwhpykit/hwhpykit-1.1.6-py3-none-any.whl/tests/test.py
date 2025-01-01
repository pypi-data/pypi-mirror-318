

from tests.ip_data import get_all_user_ip_map
from tests.user_data import get_all_user
from phone import Phone
from hwhpykit.ip.IPTransfer import IPTransfer
import xlwt


def save_data_to_excel(data_list, path):
    # 标题栏背景色
    styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour pale_blue; font: bold on;');  # 80% like
    # 创建一个工作簿
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一张表
    sheet = book.add_sheet('用户数据', cell_overwrite_ok=True)
    # 标题栏
    title_list = ('用户Id', '手机号', '手机号归属地', '网络运营商', 'IP', "IP城市")
    # 设置第一列尺寸

    first_col = sheet.col(0)
    first_col.width = 256 * 30
    # 写入标题栏
    for i in range(0, len(title_list)):
        sheet.write(0, i, title_list[i], styleBlueBkg)

    # 写入Chat信息
    for i in range(0, len(data_list)):
        data = data_list[i]
        one_data_list = [
            data.get('id'), data.get('mobile'),
            data.get('mobile_city'), data.get('mobile_type'),
            data.get('ip'), data.get('ip_city')
        ]
        for j in range(0, len(one_data_list)):
            sheet.write(i + 1, j, one_data_list[j])
    book.save(path)


if __name__ == '__main__':
    user_ip_map = get_all_user_ip_map()
    all_users = get_all_user()
    transfer = IPTransfer()
    phoneTransfer = Phone()

    for one in all_users:
        user_id = one['id']
        ip = user_ip_map.get(user_id)
        if ip:
            one['ip'] = ip
            one['ip_city'] = transfer.ip_to_city(ip)
        user_mobile = one.get('mobile')

        if 7 <= len(user_mobile) <= 11:
            info = phoneTransfer.find(user_mobile)
            if info:
                one['mobile_province'] = info.get('province')
                one['mobile_city'] = info.get('city')
                one['mobile_type'] = info.get('phone_type')
                one['mobile_zip_code'] = info.get('zip_code')
                one['city_area_code'] = info.get('area_code')

    print(all_users)
    save_data_to_excel(all_users, "./user.xls")




    # if __name__ == "__main__":
    #     phoneNum = '17613394466'
    #     info = Phone().find(phoneNum)
    #     print(info)
    #     try:
    #         phone = info['phone']
    #         province = info['province']
    #         city = info['city']
    #         zip_code = info['zip_code']
    #         area_code = info['area_code']
    #         phone_type = info['phone_type']
    #     except:
    #         print('none')

