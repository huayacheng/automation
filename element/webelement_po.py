#_*_encoding:GBK*_
# 定位元素文件

class element_position():

    # Reminder
    emc_reminder_but = "//*[@id='ctl00_ctl41_g_dc22d82a_4e03_4d40_9371_deafecd54b6d_FormControl0_V1_I1_H1']"
    # Status
    emc_Status = "//*[@id='ctl00_ctl41_g_7ba4c645_d426_41b9_b28c_a02d93d769f0_FormControl0_V1_I1_T7']"
    # eSIS Tracking    list
    # report title  r_XDKyrDO0bvnetjJG_0 fn_XDKyrDO0bvnetjJG_0 ff_XDKyrDO0bvnetjJG_0 g5_XDKyrDO0bvnetjJG_0
    emc_table_tr = "//tbody[@id='ctl00_ctl41_g_7ba4c645_d426_41b9_b28c_a02d93d769f0_FormControl0_V1_I1_R12']/*[@scriptclass='RepeatingTableRow']"

    # emc country1
    emc_table_input1 = "//input[@originalid='V1_I1_R12_I5_T1']"
    # emc country2
    emc_table_input2 = "//input[@originalid='V1_I1_R12_I6_T1']"

    # emc 模糊定位 esls tracking  //input[contains(@value,'EMC -')]
    emc_tracking_input = "//input[contains(@value,'EMC -')]"

    # emc click to view  /span[@scriptclass='HyperlinkBox']  //span[@scriptclass='HyperlinkBox']/a[contains(text(),'Click to View')]
    emc_view_a = "//tbody[@id='ctl00_ctl41_g_7ba4c645_d426_41b9_b28c_a02d93d769f0_FormControl0_V1_I1_R12']//span[@scriptclass='HyperlinkBox']//a[contains(text(),'Click to View')]"

    # 描述，单选
    # 1a.  The EMC evaluation has been completed
    def get_emc_describe(self,describe_txt):

        emc_describe_txt = "//span[contains(text(),'%s')]"%describe_txt
        return emc_describe_txt

    def get_a_describe(self,describe_txt):

        emc_describe_txt = "//a[contains(text(),'%s')]"%describe_txt
        return emc_describe_txt

    def get_div_describe(self,describe_txt):

        emc_describe_txt = "//div[contains(text(),'%s')]"%describe_txt
        return emc_describe_txt
    def get_li_describe(self,describe_txt):

        emc_describe_txt = "//li[contains(text(),'%s')]"%describe_txt
        return emc_describe_txt

    def get_input_but(self,describe_txt):
        # "//input[contains(@value,'Create packaging detail')]"
        emc_describe_txt = "//input[contains(@value,'%s')]"%describe_txt
        return emc_describe_txt

    # 单选按钮 1a,yes
    emc_option_1a_yes = "//input[@originalid='V1_I1_O13' and @checked]"
    # 单选按钮 1a,N/A
    emc_option_1a_no = "//input[@originalid='V1_I1_O14' and @checked]"
    # 单选按钮 2a,yes
    emc_option_2a_yes = "//input[@originalid='V1_I1_O15' and @checked]"
    # 单选按钮 2a,no
    emc_option_2a_no = "//input[@originalid='V1_I1_O16' and @checked]"
    # 单选按钮 3a,yes
    emc_option_3a_yes = "//input[@originalid='V1_I1_O17' and @checked]"
    # 单选按钮 3a,no
    emc_option_3a_no = "//input[@originalid='V1_I1_O18' and @checked]"
    # 单选按钮 4a,yes
    emc_option_4a_yes = "//input[@originalid='V1_I1_O19' and @checked]"
    # 单选按钮 4a,no
    emc_option_4a_no = "//input[@originalid='V1_I1_O20' and @checked]"
    # 单选按钮 5a,yes
    emc_option_5a_yes = "//input[@originalid='V1_I1_O21' and @checked]"
    # 单选按钮 5a,no
    emc_option_5a_no = "//input[@originalid='V1_I1_O22' and @checked]"


    # 提交按钮 submit
    submit_completed_but = "//input[contains(@value,'Complete') and (@type='button')]"



    # EMV
    # 状态 V1_I1_T7
    # Status
    emv_Status = "//*[@originalid='V1_I1_T7']"
    # 描述，1a
    # 单选按钮 1a,yes
    emv_option_1a_yes = "//input[@originalid='V1_I1_O12' and @checked]"
    # 单选按钮 1a,no
    emv_option_1a_no = "//input[@originalid='V1_I1_O13' and @checked]"
    # 单选按钮 2a,yes
    emv_option_2a_yes = "//input[@originalid='V1_I1_O14' and @checked]"
    # 单选按钮 2a,no
    emv_option_2a_no = "//input[@originalid='V1_I1_O15' and @checked]"
    # 单选按钮3a,yes
    emv_option_3a_yes = "//input[@originalid='V1_I1_O16' and @checked]"
    # 单选按钮 3a,no
    emv_option_3a_no = "//input[@originalid='V1_I1_O17' and @checked]"

    # setion1 status
    setion1_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I36_T2']"
    # setion2 status
    setion2_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I40_T2']"
    # setion3 status
    setion3_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I44_T2']"
    # setion4 status
    setion4_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I48_T2']"
    # setion5 status
    setion5_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I52_T2']"
    # setion6 status
    setion6_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I56_T2']"
    # setion7 status
    setion7_status = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I60_T2']"

    # Safety
    # 状态 V1_I1_T4
    # Status
    safety_Status = "//*[@originalid='V1_I1_T4']"
    # 描述，1a
    # 单选按钮 1a,yes
    safety_option_1a_yes = "//input[@originalid='V1_I1_O8' and @checked]"
    # 单选按钮 1a,no
    safety_option_1a_no = "//input[@originalid='V1_I1_O9' and @checked]"
    # 单选按钮 2a,yes
    safety_option_2a_yes = "//input[@originalid='V1_I1_O11' and @checked]"
    # 单选按钮 2a,no
    safety_option_2a_no = "//input[@originalid='V1_I1_O12' and @checked]"
    # 单选按钮 2a,N/A
    safety_option_2a_na = "//input[@originalid='V1_I1_O13' and @checked]"
    # 单选按钮3a,yes
    safety_option_3a_yes = "//input[@originalid='V1_I1_O15' and @checked]"
    # 单选按钮 3a,no
    safety_option_3a_no = "//input[@originalid='V1_I1_O16' and @checked]"
    # 单选按钮 3a,N/A
    safety_option_3a_na = "//input[@originalid='V1_I1_O17' and @checked]"
    # 单选按钮4a,yes
    safety_option_4a_yes = "//input[@originalid='V1_I1_O19' and @checked]"
    # 单选按钮 4a,no
    safety_option_4a_no = "//input[@originalid='V1_I1_O20' and @checked]"
    # 单选按钮 4a,N/A
    safety_option_4a_na = "//input[@originalid='V1_I1_O21' and @checked]"
    # 单选按钮4a,yes
    safety_option_5a_yes = "//input[@originalid='V1_I1_O23' and @checked]"
    # 单选按钮 4a,no
    safety_option_5a_no = "//input[@originalid='V1_I1_O24' and @checked]"
    # 单选按钮 5a,N/A
    safety_option_5a_na = "//input[@originalid='V1_I1_O25' and @checked]"
    # 单选按钮6a,yes
    safety_option_6a_yes = "//input[@originalid='V1_I1_O27' and @checked]"
    # 单选按钮 6a,no
    safety_option_6a_no = "//input[@originalid='V1_I1_O28' and @checked]"
    # 单选按钮 6a,N/A
    safety_option_6a_na = "//input[@originalid='V1_I1_O29' and @checked]"
    # 单选按钮7a,yes
    safety_option_7a_yes = "//input[@originalid='V1_I1_O31' and @checked]"
    # 单选按钮 7a,no
    safety_option_7a_no = "//input[@originalid='V1_I1_O32' and @checked]"
    # 单选按钮 7a,N/A
    safety_option_7a_na = "//input[@originalid='V1_I1_O33' and @checked]"
    # 单选按钮8a,yes
    safety_option_8a_yes = "//input[@originalid='V1_I1_O35' and @checked]"
    # 单选按钮 8a,no
    safety_option_8a_no = "//input[@originalid='V1_I1_O36' and @checked]"
    # 单选按钮 8a,N/A
    safety_option_8a_na = "//input[@originalid='V1_I1_O37' and @checked]"
    # 单选按钮9a,yes
    safety_option_9a_yes = "//input[@originalid='V1_I1_O39' and @checked]"
    # 单选按钮 9a,no
    safety_option_9a_no = "//input[@originalid='V1_I1_O40' and @checked]"
    # 单选按钮 9a,N/A
    safety_option_9a_na = "//input[@originalid='V1_I1_O41' and @checked]"
    # 单选按钮10a,yes
    safety_option_10a_yes = "//input[@originalid='V1_I1_O43' and @checked]"
    # 单选按钮 10a,no
    safety_option_10a_no = "//input[@originalid='V1_I1_O44' and @checked]"
    # 单选按钮 11a,N/A
    safety_option_10a_na = "//input[@originalid='V1_I1_O45' and @checked]"
    # 单选按钮11a,yes
    safety_option_11a_yes = "//input[@originalid='V1_I1_O47' and @checked]"
    # 单选按钮 11a,no
    safety_option_11a_no = "//input[@originalid='V1_I1_O48' and @checked]"
    # 单选按钮 12a,N/A
    safety_option_11a_na = "//input[@originalid='V1_I1_O49' and @checked]"
    # 单选按钮12a,yes
    safety_option_12a_yes = "//input[@originalid='V1_I1_O51' and @checked]"
    # 单选按钮 12a,no
    safety_option_12a_no = "//input[@originalid='V1_I1_O52' and @checked]"
    # 单选按钮 12a,N/A
    safety_option_12a_na = "//input[@originalid='V1_I1_O53' and @checked]"
    # 单选按钮13a,yes
    safety_option_13a_yes = "//input[@originalid='V1_I1_O55' and @checked]"
    # 单选按钮 13a,no
    safety_option_13a_no = "//input[@originalid='V1_I1_O56' and @checked]"
    # 单选按钮 13a,N/A
    safety_option_13a_na = "//input[@originalid='V1_I1_O57' and @checked]"
    # 单选按钮14a,yes
    safety_option_14a_yes = "//input[@originalid='V1_I1_O59' and @checked]"
    # 单选按钮 14a,no
    safety_option_14a_no = "//input[@originalid='V1_I1_O60' and @checked]"
    # 单选按钮 14a,N/A
    safety_option_14a_na = "//input[@originalid='V1_I1_O61' and @checked]"
    # 单选按钮15a,yes
    safety_option_15a_yes = "//input[@originalid='V1_I1_O63' and @checked]"
    # 单选按钮 15a,no
    safety_option_15a_no = "//input[@originalid='V1_I1_O64' and @checked]"
    # 单选按钮 15a,N/A
    safety_option_15a_na = "//input[@originalid='V1_I1_O65' and @checked]"
    # 单选按钮16a,yes
    safety_option_16a_yes = "//input[@originalid='V1_I1_O67' and @checked]"
    # 单选按钮 16a,no
    safety_option_16a_no = "//input[@originalid='V1_I1_O68' and @checked]"
    # 单选按钮 16a,N/A
    safety_option_16a_na = "//input[@originalid='V1_I1_O69' and @checked]"
    # 单选按钮17a,yes
    safety_option_17a_yes = "//input[@originalid='V1_I1_O71' and @checked]"
    # 单选按钮 17a,no
    safety_option_17a_no = "//input[@originalid='V1_I1_O72' and @checked]"
    # 单选按钮 17a,N/A
    safety_option_17a_na = "//input[@originalid='V1_I1_O73' and @checked]"
    # 单选按钮18a,yes
    safety_option_18a_yes = "//input[@originalid='V1_I1_O75' and @checked]"
    # 单选按钮18a,no
    safety_option_18a_no = "//input[@originalid='V1_I1_O76' and @checked]"
    # 单选按钮 18a,N/A
    safety_option_18a_na = "//input[@originalid='V1_I1_O77' and @checked]"
    # 单选按钮19a,yes
    safety_option_19a_yes = "//input[@originalid='V1_I1_O79' and @checked]"
    # 单选按钮 19a,no
    safety_option_19a_no = "//input[@originalid='V1_I1_O80' and @checked]"
    # 单选按钮 19a,N/A
    safety_option_19a_na = "//input[@originalid='V1_I1_O81' and @checked]"
    # 单选按钮20a,yes
    safety_option_20a_yes = "//input[@originalid='V1_I1_O83' and @checked]"
    # 单选按钮 7a,no
    safety_option_20a_no = "//input[@originalid='V1_I1_O84' and @checked]"
    # 单选按钮 20a,N/A
    safety_option_20a_na = "//input[@originalid='V1_I1_O85' and @checked]"
    # 单选按钮21a,yes
    safety_option_21a_yes = "//input[@originalid='V1_I1_O87' and @checked]"
    # 单选按钮21a,no
    safety_option_21a_no = "//input[@originalid='V1_I1_O88' and @checked]"
    # 单选按钮 21a,N/A
    safety_option_21a_na = "//input[@originalid='V1_I1_O89' and @checked]"
    # 单选按钮22a,yes
    safety_option_22a_yes = "//input[@originalid='V1_I1_O91' and @checked]"
    # 单选按钮 22a,no
    safety_option_22a_no = "//input[@originalid='V1_I1_O92' and @checked]"
    # 单选按钮 22a,N/A
    safety_option_22a_na = "//input[@originalid='V1_I1_O93' and @checked]"
    # 单选按钮23a,yes
    safety_option_23a_yes = "//input[@originalid='V1_I1_O95' and @checked]"
    # 单选按钮 23a,no
    safety_option_23a_no = "//input[@originalid='V1_I1_O96' and @checked]"
    # 单选按钮 23a,N/A
    safety_option_23a_na = "//input[@originalid='V1_I1_O97' and @checked]"
    # 单选按钮24a,yes
    safety_option_24a_yes = "//input[@originalid='V1_I1_O99' and @checked]"
    # 单选按钮 24a,no
    safety_option_24a_no = "//input[@originalid='V1_I1_O100' and @checked]"
    # 单选按钮 24a,N/A
    safety_option_24a_na = "//input[@originalid='V1_I1_O101' and @checked]"
    # 单选按钮25a,yes
    safety_option_25a_yes = "//input[@originalid='V1_I1_O103' and @checked]"
    # 单选按钮 25a,no
    safety_option_25a_no = "//input[@originalid='V1_I1_O104' and @checked]"
    # 单选按钮 25a,N/A
    safety_option_25a_na = "//input[@originalid='V1_I1_O105' and @checked]"
    # 单选按钮26a,yes
    safety_option_26a_yes = "//input[@originalid='V1_I1_O107' and @checked]"
    # 单选按钮 26a,no
    safety_option_26a_no = "//input[@originalid='V1_I1_O108' and @checked]"
    # 单选按钮 26a,N/A
    safety_option_26a_na = "//input[@originalid='V1_I1_O109' and @checked]"
    # 单选按钮27a,yes
    safety_option_27a_yes = "//input[@originalid='V1_I1_O111' and @checked]"
    # 单选按钮 27a,no
    safety_option_27a_no = "//input[@originalid='V1_I1_O112' and @checked]"
    # 单选按钮 27a,N/A
    safety_option_27a_na = "//input[@originalid='V1_I1_O113' and @checked]"
    # 单选按钮28a,yes
    safety_option_28a_yes = "//input[@originalid='V1_I1_O115' and @checked]"
    # 单选按钮 28a,no
    safety_option_28a_no = "//input[@originalid='V1_I1_O116' and @checked]"
    # 单选按钮 28a,N/A
    safety_option_28a_na = "//input[@originalid='V1_I1_O117' and @checked]"
    # 单选按钮29a,yes
    safety_option_29a_yes = "//input[@originalid='V1_I1_O119' and @checked]"
    # 单选按钮 29a,no
    safety_option_29a_no = "//input[@originalid='V1_I1_O120' and @checked]"
    # 单选按钮 29a,N/A
    safety_option_29a_na = "//input[@originalid='V1_I1_O121' and @checked]"
    # 单选按钮 30a,yes
    safety_option_30a_yes = "//input[@originalid='V1_I1_O123' and @checked]"
    # 单选按钮 30a,no
    safety_option_30a_no = "//input[@originalid='V1_I1_O124' and @checked]"
    # 单选按钮 30a,N/A
    safety_option_30a_na = "//input[@originalid='V1_I1_O125' and @checked]"
    # 单选按钮 31a,yes
    safety_option_31a_yes = "//input[@originalid='V1_I1_O127' and @checked]"
    # 单选按钮 31a,no
    safety_option_31a_no = "//input[@originalid='V1_I1_O128' and @checked]"
    # 单选按钮 31a,N/A
    safety_option_31a_na = "//input[@originalid='V1_I1_O129' and @checked]"
    # 单选按钮 32a,yes
    safety_option_32a_yes = "//input[@originalid='V1_I1_O131' and @checked]"
    # 单选按钮 32a,no
    safety_option_32a_no = "//input[@originalid='V1_I1_O132' and @checked]"
    # 单选按钮 32a,N/A
    safety_option_32a_na = "//input[@originalid='V1_I1_O133' and @checked]"
    # 单选按钮 33a,yes
    safety_option_33a_yes = "//input[@originalid='V1_I1_O135' and @checked]"
    # 单选按钮 33a,no
    safety_option_33a_no = "//input[@originalid='V1_I1_O136' and @checked]"
    # 单选按钮 33a,N/A
    safety_option_33a_na = "//input[@originalid='V1_I1_O137' and @checked]"
    # 单选按钮 34a,yes
    safety_option_34a_yes = "//input[@originalid='V1_I1_O139' and @checked]"
    # 单选按钮 34a,no
    safety_option_34a_no = "//input[@originalid='V1_I1_O140' and @checked]"
    # 单选按钮 34a,N/A
    safety_option_34a_na = "//input[@originalid='V1_I1_O141' and @checked]"
    # 单选按钮 35a,yes
    safety_option_35a_yes = "//input[@originalid='V1_I1_O143' and @checked]"
    # 单选按钮 35a,no
    safety_option_35a_no = "//input[@originalid='V1_I1_O144' and @checked]"

    # 单选按钮 36a,yes
    safety_option_36a_yes = "//input[@originalid='V1_I1_O146' and @checked]"
    # 单选按钮 36a,no
    safety_option_36a_no = "//input[@originalid='V1_I1_O147' and @checked]"


    # PERD——form

    # section - 1 名称
    section1_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I36_T1' and @title]"
    section1_click_but = "//a[contains(text(),'click here to view Section 1')]"
    section1_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I36']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 1 状态
    # section - 2 名称
    section2_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I40_T1' and @title]"
    section2_click_but = "//a[contains(text(),'click here to view Section 2')]"
    section2_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I40']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 2 状态
    # section - 3 名称
    section3_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I44_T1' and @title]"
    section3_click_but = "//a[contains(text(),'click here to view Section 3')]"
    section3_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I44']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 3 状态
    # section - 4 名称
    section4_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I48_T1' and @title]"
    section4_click_but = "//a[contains(text(),'click here to view Section 4')]"
    section4_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I48']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 4 状态
    # section - 5 名称
    section5_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I52_T1' and @title]"
    section5_click_but = "//a[contains(text(),'click here to view Section 5')]"
    section5_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I52']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 5 状态
    # section - 6 名称
    section6_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I56_T1' and @title]"
    section6_click_but = "//a[contains(text(),'click here to view Section 6')]"
    section6_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I56']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 6 状态
    # section - 7 名称
    section7_title = "//input[@originalid='V1_I1_S8_I34_S3_I35_R1_I60_T1' and @title]"
    section7_click_but = "//a[contains(text(),'click here to view Section 7')]"
    section7_status = "//tr[@originalid='V1_I1_S8_I34_S3_I35_R1_I60']//div[@class='hc_CsB83gH6oS4UDkd9_0']//span[@class='b0_CsB83gH6oS4UDkd9_0']"  # section - 7 状态

    # Geo Packaging Record 1000mm
    section4_packaging_edit = "//span[contains(text(),'编辑项目')]"

    # Overall size of sales packaging
    section4_packaging_input_1a = "//input[@originalid='V1_I1_T9']"
    section4_packaging_input_2a = "//input[@originalid='V1_I1_T10']"
    section4_packaging_input_3a = "//input[@originalid='V1_I1_T11']"
    section4_packaging_input_4a = "//input[@originalid='V1_I1_T12']"
    section4_packaging_input_5a = "//input[@originalid='V1_I1_T13']"
    section4_packaging_input_6a = "//input[@originalid='V1_I1_T14']"
    section4_packaging_input_7a = "//input[@originalid='V1_I1_T15']"
    section4_packaging_input_8a = "//input[@originalid='V1_I1_T16']"

    # Create Packaging Detail
    section4_create_input_but = "//input[contains(@value,'Create Packaging Detail')]"
    section4_refresh_input_but = "//input[contains(@value,'Refresh Packaging Detail')]"

    # section4 refresh geo   "//input[@]
    section4_refresh_packaging_input_but = "//input[contains(@value,'Refresh Geo Packaging')]"

    # Click to view  //a[contains(@text,'Click to view' and (@tabindex=0))]
    section4_sales_input_a = "//a[contains(text(),'Click to view')]"
    #Select Packaging Type
    packaging_record_select_1a = "//select[@originalid='V1_I1_D7']"
    packaging_record_select_2a = "//select[@originalid='V1_I1_D8']"
    packaging_record_select_3a = "//select[@originalid='V1_I1_D9']"


    packaging_record_input_1a = "//input[@originalid='V1_I1_T10']"
    packaging_record_input_2a = "//input[@originalid='V1_I1_T11']"
    packaging_record_input_select_2a = "//input[@originalid='V1_I1_D8']"
    # 提交按钮
    packaging_submit_but = "//input[contains(@value,'Submit') and (@type='button')]"
    # 保存按钮
    packaging_Record_save_but = "//input[contains(@value,'Save & Close') and (@type='button')]"

    # section - 1 product descripution
    section1_select = "//select[@originalid='V1_I1_S1_I1_S5_I8_D1']"
    # 1.2
    section1_option_1a_yes = "//input[@originalid='V1_I1_S1_I1_O7']"
    section1_option_1a_no = "//input[@originalid='V1_I1_S1_I1_O8']"
    section1_input_general_1a = "//textarea[@originalid='V1_I1_S1_I1_S9_I11_T1']"

    # 1.3 输入
    section1_input_1t = "//input[@originalid='V1_I1_S1_I1_T10']"
    section1_input_2t = "//input[@originalid='V1_I1_S1_I1_T11']"
    section1_input_3t = "//input[@originalid='V1_I1_S1_I1_T12']"
    section1_input_4t = "//input[@originalid='V1_I1_S1_I1_T13']"
    section1_input_5t = "//input[@originalid='V1_I1_S1_I1_T14']"
    section1_input_6t = "//input[@originalid='V1_I1_S1_I1_T15']"
    section1_input_7t = "//input[@originalid='V1_I1_S1_I1_T16']"
    section1_input_8t = "//input[@originalid='V1_I1_S1_I1_T17']"
    # option  V1_I1_S1_I1_O18              FormControl_V1_I1_S1_I1_O18
    section1_option_da_yes = "//input[@id='FormControl_V1_I1_S1_I1_O18']"
    section1_option_da_no = "//input[@id='FormControl_V1_I1_S1_I1_O19']"
    #  Does this product have a screen? option
    section1_input_screen_1a = "//input[@originalid='V1_I1_S1_I1_S20_I12_T1']"
    section1_input_screen_2a = "//input[@originalid='V1_I1_S1_I1_S20_I12_T2']"
    section1_click_screen_3a = "//input[@originalid='V1_I1_S1_I1_S20_I12_B3']"
    section1_click_screen_4a = "//input[@originalid='V1_I1_S1_I1_S20_I12_B4']"
    # will 1a option
    section1_will_option_yes = "//input[@originalid='V1_I1_S1_I1_S25_I18_O1']"
    section1_will_option_no = "//input[@originalid='V1_I1_S1_I1_S25_I18_O2']"
    # will 2a option
    section2_will_option_yes = "//input[@originalid='V1_I1_S1_I1_S25_I18_O3']"
    section2_will_option_no = "//input[@originalid='V1_I1_S1_I1_S25_I18_O4']"
    # will 3a option
    section3_will_option_yes = "//input[@originalid='V1_I1_S1_I1_S25_I18_O5']"
    section3_will_option_no = "//input[@originalid='V1_I1_S1_I1_S25_I18_O6']"
    # 1.5 radio
    # will 4a option   V1_I1_S1_I1_O26  FormControl_V1_I1_S1_I1_O26
    section4_will_option_yes = "//input[@id='FormControl_V1_I1_S1_I1_O26']"
    section4_will_option_no = "//input[@id='FormControl_V1_I1_S1_I1_O27']"

    # inputs
    section1_company_input_1a = "//input[@originalid='V1_I1_S1_I1_S28_I20_T1']"
    section1_company_input_2a = "//input[@originalid='V1_I1_S1_I1_S28_I20_T2']"
    section1_company_input_3a = "//input[@originalid='V1_I1_S1_I1_S28_I20_T3']"
    section1_company_input_4a = "//input[@originalid='V1_I1_S1_I1_S28_I20_T4']"
    section1_company_input_5a = "//input[@originalid='V1_I1_S1_I1_S28_I20_T5']"

    # Attachments
    section1_attachments_input_1a = "//input[@originalid='V1_I1_T1']"
    section1_attachments_select_3a = "//select[@originalid='V1_I1_D4']"
    section1_attachments_select_4a = "//select[@originalid='V1_I1_D5']"
    section1_attachments_input_5a = "//div[@id='ctl00_ctl41_g_c7d30b9c_34c7_4c10_8c79_7677ec8ea9c9_FormControl0_V1_I1_RTC6_RTI2_RT1_newRichText']"

    #  上传之后的元素  V1_I1_SPFAC3_SPI3_SPFA1
    section1_spfa_text1 = "//span[@originalid='V1_I1_SPFAC3_SPI3_SPFA1']"
    # 保存按钮
    section1_attachments_savebut = "//input[contains(@value,'Save & Close')]"

    # section - 2 product descripution
    section2_select = "//select[@originalid='V1_I1_S1_I1_T4' and @disabled='title']"  # 当前状态
    # 2.1
    # 通用的section——option
    section2_option = "//input[@scriptclass='RadioButton']"
    # 非通用精准定位
    # 2.1
    section2_option_2a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_O2']"
    section2_option_2a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_O3']"
    # 2.2
    section2_option_3a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_O1']"
    section2_option_3a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_O2']"
    # 2.2.2                                  V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S4_I15_S1_I16_FAC1_FAI17_F1
    # 2.2.2a
    section2_click1_2a = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S3_I8_S1_I9_FAC1_FAI10_F1']"
    section2_click2_2a = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S3_I8_S3_I12_FAC1_FAI13_F1']"
    # 2.2.21
    section2_click_a = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S4_I15_S1_I16_FAC1_FAI17_F1']"
    # 2.2.3 输入框
    section2_input = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_T5']"
    # 2.2.4 单选
    section2_option_4a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_O6']"
    section2_option_4a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_O7']"
    # 2.2.5 输入框，P/N
    section2_input1_5a = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S8_I19_R1_I20_T1']"
    section2_input2_5a = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S8_I19_R1_I20_T2']"
    section2_input3_5a = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S8_I19_R1_I20_T3']"
    section2_input4_5a = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S8_I19_R1_I20_T4']"
    # 2.2.5.1 上传
    section2_click25_a1 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S9_I21_S1_I22_FAC1_FAI23_F1']"
    # 2.2.5.2 上传
    section2_click25_a2 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S9_I21_S3_I25_FAC1_FAI26_F1']"
    # 2.3 Measured Heat Output
    section2_measured_input_a1 = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_T10']"
    section2_measured_input_a2 = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_T11']"
    # 2.4
    section2_select_a = "//select[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_D13']"
    section2_select_inputs = "//textarea[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S1_I7_S14_I28_T1']"
    #2.5 单选
    section2_option_5a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O1']"
    section2_option_5a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O2']"
    section2_click_cecp_a = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S3_I38_S1_I39_FAC1_FAI40_F1']"
    # input
    section2_cecp_input = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S3_I38_T3']"
    # 2.6 单选
    section2_option_6a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O4']"
    section2_option_6a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O5']"
    section2_option_6a_click_a = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S6_I42_S3_I43_FAC1_FAI44_F1']"
    # 2.7 单选
    section2_option_7a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O7']"
    section2_option_7a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O8']"
    # 2.7.2
    section2_option2_7a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S9_I46_O1']"
    section2_option2_7a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S9_I46_O2']"
    section2_input_date = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S10_I47_T1']"
    # 2.8 单选
    section2_option_8a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O11']"
    section2_option_8a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O12']"
    # 2.9 单选
    # 2.9.1
    section2_option_9a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O13']"
    section2_option_9a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_O14']"
    # 2.9.2
    section2_select_9a = "//select[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_D1']"
    # 2.9.3 Desktop
    section2_option_10a_yes = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S2_I49_O1']"
    section2_option_10a_no = "//input[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S2_I49_O2']"
    # 2.9.3
    section2_click293_a1 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S3_I56_S1_I57_FAC1_FAI58_F1']"
    section2_click293_a2 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S5_I64_S1_I65_FAC1_FAI66_F1']"
    section2_click293_a3 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S4_I60_S1_I61_FAC1_FAI62_F1']"
    section2_click293_a4 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S6_I68_S1_I69_FAC1_FAI70_F1']"
    section2_click293_a5 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S7_I72_S1_I73_FAC1_FAI74_F1']"

    section2_click293_img = "//img[@alt='文件附件菜单。']"
    section2_del_a = "//a[contains(text(),'删除')]"
    # 2.9.4 上传按钮
    section2_click294_a1 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S2_I49_S3_I50_FAC1_FAI51_F1']"
    section2_click294_a2 = "//a[@originalid='V1_I1_S1_I1_S9_I5_S4_I6_S2_I37_S15_I48_S2_I49_S5_I52_S1_I53_FAC1_FAI54_F1']"
    # Section 3
    # 3.1.1
    section3_select_1a = "//select[@originalid='V1_I1_S2_I5_D2']"
    section3_input_1a = "//input[@originalid='V1_I1_S2_I5_S3_I6_T1']"
    section3_input_2a = "//input[@originalid='V1_I1_S2_I5_S3_I6_T2']"
    # 3.1.2
    section3_select_2a = "//select[@originalid='V1_I1_S2_I5_D4']"
    section3_input_3a = "//input[@originalid='V1_I1_S2_I5_S5_I7_T1']"
    section3_click_a = "//a[@originalid='V1_I1_S2_I5_S7_I8_FAC1_FAI9_F1']"
    # 3.2
    # 3.2.1
    section3_select2_1a = "//select[@originalid='V1_I1_S2_I5_D9']"
    # 3.2.1a
    section3_select2_1a2 = "//select[@originalid='V1_I1_S2_I5_S10_I11_D1']"
    # 3.2.2
    section3_option_1a_yes = "//input[@originalid='V1_I1_S2_I5_O11']"
    section3_option_1a_no = "//input[@originalid='V1_I1_S2_I5_O12']"
    # 3.2.2.a
    section3_select3a_1a = "//select[@originalid='V1_I1_S2_I5_S13_I12_D1']"
    section3_select_input3a_2a = "//input[@originalid='V1_I1_S2_I5_S13_I12_S2_I13_T1']"
    section3_input3b_2a = "//input[@originalid='V1_I1_S2_I5_S13_I12_T3']"
    section3_input3c_3a = "//input[@originalid='V1_I1_S2_I5_S13_I12_T4']"
    section3_input3d_4a = "//input[@originalid='V1_I1_S2_I5_S13_I12_T5']"
    # 3.2.3
    section3_select2_2a = "//select[@originalid='V1_I1_S2_I5_D14']"
    # 3.2.4
    section3_select2_3a = "//select[@originalid='V1_I1_S2_I5_D15']"
    section3_input2_3a = "//input[@originalid='V1_I1_S2_I5_S16_I14_T1']"
    # 3.2.5
    section3_option_2a_yes = "//input[@originalid='V1_I1_S2_I5_O17']"
    section3_option_2a_no = "//input[@originalid='V1_I1_S2_I5_O18']"
    # 3.2.5 a
    section3_option_3a_yes = "//input[@originalid='V1_I1_S2_I5_S19_I15_O1']"
    section3_option_3a_no = "//input[@originalid='V1_I1_S2_I5_S19_I15_O2']"
    section3_option_3a_input = "//input[@originalid='V1_I1_S2_I5_S19_I15_S3_I16_T1']"
    # 3.2.5 b
    section3_option_4a_yes = "//input[@originalid='V1_I1_S2_I5_S19_I15_O4']"
    section3_option_4a_no = "//input[@originalid='V1_I1_S2_I5_S19_I15_O5']"
    section3_option_4a_input = "//input[@originalid='V1_I1_S2_I5_S19_I15_S6_I17_T1']"
    # Identify the location.

    # 3.2.5 c
    section3_option_5a_yes = "//input[@originalid='V1_I1_S2_I5_S19_I15_O7']"
    section3_option_5a_no = "//input[@originalid='V1_I1_S2_I5_S19_I15_O8']"
    section3_option_5a_input1 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S9_I18_T1']"
    section3_option_5a_input2 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S9_I18_T2']"
    # 3.2.5 d
    section3_option_6a_yes = "//input[@originalid='V1_I1_S2_I5_S19_I15_O10']"
    section3_option_6a_no = "//input[@originalid='V1_I1_S2_I5_S19_I15_O11']"
    section3_option_6a_input = "//input[@originalid='V1_I1_S2_I5_S19_I15_S12_I19_T1']"
    # 3.2.5 e
    section3_option_7a_yes = "//input[@originalid='V1_I1_S2_I5_S19_I15_O13']"
    section3_option_7a_no = "//input[@originalid='V1_I1_S2_I5_S19_I15_O14']"
    section3_option_7a_input1 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S15_I20_T1']"
    section3_option_7a_input2 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S15_I20_T2']"
    section3_option_7a_input3 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S15_I20_T3']"
    # 3.2.5 f
    section3_option_8a_yes = "//input[@originalid='V1_I1_S2_I5_S19_I15_O16']"
    section3_option_8a_no = "//input[@originalid='V1_I1_S2_I5_S19_I15_O17']"
    section3_option_8a_input1 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S18_I21_T1']"
    section3_option_8a_input2 = "//input[@originalid='V1_I1_S2_I5_S19_I15_S18_I21_T2']"
    # 3.2.6
    section3_option_9a_yes = "//input[@originalid='V1_I1_S2_I5_O20']"
    section3_option_9a_no = "//input[@originalid='V1_I1_S2_I5_O21']"
    section3_option_9a_select1 = "//select[@originalid='V1_I1_S2_I5_R23_I23_D1']"
    section3_option_9a_input2 = "//textarea[@originalid='V1_I1_S2_I5_R23_I23_T2']"
    section3_option_9a_input3 = "//textarea[@originalid='V1_I1_S2_I5_R23_I23_T3']"
    section3_option_9a_input4 = "//textarea[@originalid='V1_I1_S2_I5_R23_I23_T4']"
    section3_option_9a_input5 = "//textarea[@originalid='V1_I1_S2_I5_R23_I23_T5']"
    section3_option_9a_input6 = "//input[@originalid='V1_I1_S2_I5_R23_I23_T6']"

    # 3.3 Battery Information
    section3_option_10a_yes = "//input[@originalid='V1_I1_S2_I5_O25']"
    section3_option_10a_no = "//input[@originalid='V1_I1_S2_I5_O26']"
    section3_click_10a_but1 = "//input[@originalid='V1_I1_S2_I5_S27_I24_B2']"
    section3_click_10a_but2 = "//input[@originalid='V1_I1_S2_I5_S27_I24_B3']"
    # 3.4 Lasers
    section3_option_11a_yes = "//input[@originalid='V1_I1_S2_I5_O28']"
    section3_option_11a_no = "//input[@originalid='V1_I1_S2_I5_O29']"
    section3_option_11a_input = "//input[@originalid='V1_I1_S2_I5_S30_I25_T1']"
    # 3.4 Please indicate how you will provide the laser data.
    section3_option_11a_Attachment = "//input[@originalid='V1_I1_S2_I5_S31_I29_O1']"
    section3_option_11a_LaserTable = "//input[@originalid='V1_I1_S2_I5_S31_I29_O2']"
    # Attachment
    section3_option_11a_click_a = "//a[@originalid='V1_I1_S2_I5_S31_I29_S3_I30_S1_I31_FAC1_FAI32_F1']"
    # Laser Table
    section3_select_11a_1a = "//select[@originalid='V1_I1_S2_I5_S31_I27_S4_I32_R1_I33_D1']"
    section3_select_11a_2a = "//select[@originalid='V1_I1_S2_I5_S31_I27_S4_I32_R1_I33_D2']"
    section3_select_11a_3a = "//select[@originalid='V1_I1_S2_I5_S31_I27_S4_I32_R1_I33_D3']"
    section3_input_11a_1a = "//input[@originalid='V1_I1_S2_I5_S31_I27_S4_I32_R1_I33_T4']"
    # Insert item
    # section3_11a_click_a_item = "//a[@originalid='V1_I1_S2_I5_S31_I27_S3_I28_S1_I29_FAC1_FAI30_F1']"
    # 3.5 Pressurized Parts
    section3_option_12a_yes = "//input[@originalid='V1_I1_S2_I5_O32']"
    section3_option_12a_no = "//input[@originalid='V1_I1_S2_I5_O33']"
    section3_option_12a_input = "//input[@originalid='V1_I1_S2_I5_T34']"
    section3_option_12a_list_1a = "//input[@originalid='V1_I1_S2_I5_S35_I36_R1_I37_T1']"
    section3_option_12a_list_2a = "//input[@originalid='V1_I1_S2_I5_S35_I36_R1_I37_T2']"
    # 3.6 Finishes
    section3_option_13a_yes = "//input[@originalid='V1_I1_S2_I5_O36']"
    section3_option_13a_no = "//input[@originalid='V1_I1_S2_I5_O37']"
    section3_option_13a_input = "//input[@originalid='V1_I1_S2_I5_T38']"

    # 3.7 Finishes
    section3_option_14a_yes = "//input[@originalid='V1_I1_S2_I5_O39']"
    section3_option_14a_no = "//input[@originalid='V1_I1_S2_I5_O40']"

    # 3.7 input
    section3_option_14a_input = "//input[@originalid='V1_I1_S2_I5_T41']"

    section3_option_14a_list_1a = "//input[@originalid='V1_I1_S2_I5_S42_I38_R1_I39_T1']"
    section3_option_14a_list_2a = "//input[@originalid='V1_I1_S2_I5_S42_I38_R1_I39_T2']"
    section3_option_14a_list_3a = "//input[@originalid='V1_I1_S2_I5_S42_I38_R1_I39_T3']"
    # Section 4
    # 4.1 Field Use Material (FUM)
    section4_option_1a_yes = "//input[@originalid='V1_I1_S2_I7_S1_I8_O2']"
    section4_option_1a_no = "//input[@originalid='V1_I1_S2_I7_S1_I8_O3']"
    section4_option_input_1a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_T1']"
    section4_option_1a_list_1a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_R2_I10_T1']"
    section4_option_1a_list_2a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_R2_I10_T2']"
    section4_option_1a_list_3a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_R2_I10_T3']"
    section4_option_1a_list_4a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_R2_I10_T4']"
    section4_option_1a_list_5a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_R2_I10_T5']"
    section4_option_1a_select6 = "//select[@originalid='V1_I1_S2_I7_S1_I8_S4_I9_R2_I10_D6']"

    # 4.2 Additional Chemicals
    section4_option_2a_yes = "//input[@originalid='V1_I1_S2_I7_S1_I8_O5']"
    section4_option_2a_no = "//input[@originalid='V1_I1_S2_I7_S1_I8_O6']"

    section4_option_2a_list_1a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S8_I11_R1_I12_T1']"
    section4_option_2a_list_2a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S8_I11_R1_I12_T2']"
    section4_option_2a_list_3a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S8_I11_R1_I12_T3']"
    # 4.2 input
    section4_option_2a_input = "//input[@originalid='V1_I1_S2_I7_S1_I8_T7']"
    # 4.3 Chemical Waste
    section4_option_3a_yes = "//input[@originalid='V1_I1_S2_I7_S1_I8_O9']"
    section4_option_3a_no = "//input[@originalid='V1_I1_S2_I7_S1_I8_O10']"
    section4_option_3a_list_1a = "//input[@originalid='V1_I1_S2_I7_S1_I8_S12_I13_R1_I14_T1']"
    # 4.3 input
    section4_option_3a_input = "//input[@originalid='V1_I1_S2_I7_S1_I8_T11']"
    #4.4 Packaging Information
    section4_option_4a_1a = "//span[@originalid='V1_I1_S2_I7_S1_I8_R13_I15_HB1']//a[contains(text(),'Click to view')]"
    section4_option_4a_2a = "//span[@originalid='V1_I1_S2_I7_S1_I8_R13_I17_HB1']//a[contains(text(),'Click to view')]"
    # status
    section4_option_4a_status_1 = "//input[@originalid='V1_I1_S2_I7_S1_I8_R13_I15_T6']"
    section4_option_4a_status_2 = "//input[@originalid='V1_I1_S2_I7_S1_I8_R13_I17_T6']"

    # 4.4, page TOPT-2020-0036 - AG (America Group) - 5214
    section4_page_input_1a = "//input[@originalid='V1_I1_T9']"
    section4_page_input_2a = "//input[@originalid='V1_I1_T10']"
    section4_page_input_3a = "//input[@originalid='V1_I1_T11']"
    section4_page_input_4a = "//input[@originalid='V1_I1_T12']"
    section4_page_input_5a = "//input[@originalid='V1_I1_T13']"
    section4_page_input_6a = "//input[@originalid='V1_I1_T14']"
    section4_page_input_7a = "//input[@originalid='V1_I1_T15']"
    section4_page_input_8a = "//input[@originalid='V1_I1_T16']"

    # 4.4, page TOPT-2020-0036 - EMEA (Europe, Middle East and Africa) - 5215
    section4_page_input2_1a = "//span[@originalid='V1_I1_T9']"
    section4_page_input2_2a = "//span[@originalid='V1_I1_T10']"
    section4_page_input2_3a = "//span[@originalid='V1_I1_T11']"
    section4_page_input2_4a = "//span[@originalid='V1_I1_T12']"
    section4_page_input2_5a = "//span[@originalid='V1_I1_T13']"
    section4_page_input2_6a = "//span[@originalid='V1_I1_T14']"
    section4_page_input2_7a = "//span[@originalid='V1_I1_T15']"
    section4_page_input2_8a = "//span[@originalid='V1_I1_T16']"


    # Geo Packaging Record
    packagin_input_1a = "//input[@originalid='V1_I1_T9']"
    packagin_input_2a = "//input[@originalid='V1_I1_T10']"
    packagin_input_3a = "//input[@originalid='V1_I1_T11']"
    packagin_input_4a = "//input[@originalid='V1_I1_T12']"
    packagin_input_5a = "//input[@originalid='V1_I1_T13']"
    packagin_input_6a = "//input[@originalid='V1_I1_T14']"
    packagin_input_7a = "//input[@originalid='V1_I1_T15']"
    packagin_input_8a = "//input[@originalid='V1_I1_T16']"








    # Section 5 Environmental Product Design

    # 5.1 Product Features
    section5_option_1a_yes = "//input[@originalid='V1_I1_S2_I5_O2']"
    section5_option_1a_no = "//input[@originalid='V1_I1_S2_I5_O3']"
    # 5.1 input
    section5_design_input_1a = "//input[@originalid='V1_I1_S2_I5_T4']"
    # 5.2  Energy Controls
    section5_option_2a_yes = "//input[@originalid='V1_I1_S2_I5_O5']"
    section5_option_2a_no = "//input[@originalid='V1_I1_S2_I5_O6']"
    # 5.2 input
    section5_design_input_2a = "//input[@originalid='V1_I1_S2_I5_T7']"
    # 5.3 Product Disposal
    section5_option_3a_yes = "//input[@originalid='V1_I1_S2_I5_O8']"
    section5_option_3a_no = "//input[@originalid='V1_I1_S2_I5_O9']"
    section5_option_3a_no_parts = "//input[@originalid='V1_I1_S2_I5_O10']"
    # 5.3 input
    section5_design_input_3a = "//input[@originalid='V1_I1_S2_I5_T11']"
    # 5.4 Common Parts
    section5_option_4a_yes = "//input[@originalid='V1_I1_S2_I5_O12']"
    section5_option_4a_no = "//input[@originalid='V1_I1_S2_I5_O13']"
    # 5.4 input
    section5_design_input_4a = "//input[@originalid='V1_I1_S2_I5_T14']"
    # 5.5 Product Documentation
    section5_checkbox_5a_1b = "//input[@originalid='V1_I1_S2_I5_C15']"
    section5_checkbox_5a_2b = "//input[@originalid='V1_I1_S2_I5_C16']"
    section5_checkbox_5a_3b = "//input[@originalid='V1_I1_S2_I5_C17']"
    section5_checkbox_5a_4b = "//input[@originalid='V1_I1_S2_I5_C18']"
    section5_checkbox_5a_5b = "//input[@originalid='V1_I1_S2_I5_C19']"
    section5_checkbox_5a_6b = "//input[@originalid='V1_I1_S2_I5_C20']"
    section5_checkbox_5a_7b = "//input[@originalid='V1_I1_S2_I5_C21']"

    section5_textarea_5a_input1 = "//textarea[@originalid='V1_I1_S2_I5_S22_I6_T1']"
    section5_textarea_5a_input2 = "//textarea[@originalid='V1_I1_S2_I5_S23_I7_T1']"
    # 5.6 Upgradeability and Expandability
    section5_checkbox_6a_1b = "//input[@originalid='V1_I1_S2_I5_C24']"
    section5_checkbox_6a_2b = "//input[@originalid='V1_I1_S2_I5_C25']"
    section5_checkbox_6a_3b = "//input[@originalid='V1_I1_S2_I5_C26']"
    section5_checkbox_6a_4b = "//input[@originalid='V1_I1_S2_I5_C27']"
    section5_checkbox_6a_5b = "//input[@originalid='V1_I1_S2_I5_C28']"
    section5_checkbox_6a_6b = "//input[@originalid='V1_I1_S2_I5_C29']"
    section5_checkbox_6a_7b = "//input[@originalid='V1_I1_S2_I5_C30']"
    section5_checkbox_6a_8b = "//input[@originalid='V1_I1_S2_I5_C31']"
    section5_checkbox_6a_9b = "//input[@originalid='V1_I1_S2_I5_C32']"

    # input
    section5_text_6a_input1_1a = "//input[@originalid='V1_I1_S2_I5_S33_I8_T1']"
    section5_text_6a_input2_2c1 = "//input[@originalid='V1_I1_S2_I5_S34_I9_T1']"
    section5_text_6a_input2_2c2 = "//input[@originalid='V1_I1_S2_I5_S34_I9_T2']"
    section5_text_6a_input3_3d1 = "//input[@originalid='V1_I1_S2_I5_S35_I10_T1']"
    section5_text_6a_input3_3d2 = "//input[@originalid='V1_I1_S2_I5_S35_I10_T2']"
    section5_text_6a_input4_4e = "//input[@originalid='V1_I1_S2_I5_S36_I11_T1']"
    section5_text_6a_input5_5f = "//input[@originalid='V1_I1_S2_I5_S37_I12_T1']"
    section5_text_6a_input6_6h = "//textarea[@originalid='V1_I1_S2_I5_S38_I13_T1']"




    section5_option_6a_yes = "//input[@originalid='V1_I1_S2_I5_O39']"
    section5_option_6a_no = "//input[@originalid='V1_I1_S2_I5_O40']"
    section5_design_input_6a = "//input[@originalid='V1_I1_S2_I5_T41']"
    # 5.7 Ease of Repair
    section5_checkbox_7a_1b = "//input[@originalid='V1_I1_S2_I5_C42']"
    section5_checkbox_7a_2b = "//input[@originalid='V1_I1_S2_I5_C43']"
    section5_checkbox_7a_3b = "//input[@originalid='V1_I1_S2_I5_C44']"
    section5_checkbox_7a_4b = "//input[@originalid='V1_I1_S2_I5_C45']"
    section5_checkbox_7a_5b = "//input[@originalid='V1_I1_S2_I5_C46']"

    # input
    section5_text_7a_input1_d = "//textarea[@originalid='V1_I1_S2_I5_S47_I14_T1']"

    # 5.8 Plastic Parts
    section5_option_8a_yes = "//input[@originalid='V1_I1_S2_I5_O48']"
    section5_option_8a_no = "//input[@originalid='V1_I1_S2_I5_O49']"
    section5_design_input_8a = "//input[@originalid='V1_I1_S2_I5_T50']"
    # 5.9 Plastic Parts
    section5_option_9a_yes = "//input[@originalid='V1_I1_S2_I5_O51']"
    section5_option_9a_no = "//input[@originalid='V1_I1_S2_I5_O52']"
    section5_design_input_9a = "//input[@originalid='V1_I1_S2_I5_T54']"
    # % 选项
    section5_design_input1_9a = "//input[@originalid='V1_I1_S2_I5_S53_I15_T1']"
    # List information for those plastic parts identified as containing recycled content.
    section5_design_textarea_1a = "//textarea[@originalid='V1_I1_S2_I5_S55_I16_R1_I17_T1']"
    section5_design_textarea_2a = "//textarea[@originalid='V1_I1_S2_I5_S55_I16_R1_I17_T2']"
    section5_design_textarea_3a = "//textarea[@originalid='V1_I1_S2_I5_S55_I16_R1_I17_T3']"
    section5_design_textarea_4a = "//textarea[@originalid='V1_I1_S2_I5_S55_I16_R1_I17_T4']"
    section5_design_textarea_5a = "//textarea[@originalid='V1_I1_S2_I5_S55_I16_R1_I17_T5']"

    # 5.10 Recycling Efforts
    section5_design_input1_10a = "//input[@originalid='V1_I1_S2_I5_T56']"
    section5_design_input2_10a = "//input[@originalid='V1_I1_S2_I5_T57']"
    # 5.11  Printer Features
    section5_checkbox_11a_1b = "//input[@originalid='V1_I1_S2_I5_C58']"
    section5_checkbox_11a_2b = "//input[@originalid='V1_I1_S2_I5_C59']"
    section5_checkbox_11a_3b = "//input[@originalid='V1_I1_S2_I5_C60']"
    section5_checkbox_11a_4b = "//input[@originalid='V1_I1_S2_I5_C61']"

    # input
    section5_textarea_11a_1b = "//textarea[@originalid='V1_I1_S2_I5_S62_I18_T1']"
    section5_textarea_11a_2c = "//textarea[@originalid='V1_I1_S2_I5_S63_I19_T1']"

    # Section 6  Emissions Data
    # 6.1 Chemical Emissions
    section6_option_1a_yes = "//input[@originalid='V1_I1_S2_I5_O2']"
    section6_option_1a_no = "//input[@originalid='V1_I1_S2_I5_O3']"
    section6_option_1a_not = "//input[@originalid='V1_I1_S2_I5_O4']"
    section6_emiss_input_1a = "//input[@originalid='V1_I1_S2_I5_S8_I15_T1']"

    # 上传
    section6_updata_1a_a = "//a[@originalid='V1_I1_S2_I5_S7_I11_S1_I12_FAC1_FAI13_F1']"

    section6_option_1a_letter_yes = "//input[@originalid='V1_I1_S2_I5_S5_I6_O1']"
    section6_option_1a_letter_no = "//input[@originalid='V1_I1_S2_I5_S5_I6_O2']"
    # 6.2.yes 上传
    section6_letter_updata_1a = "//a[@originalid='V1_I1_S2_I5_S6_I7_S1_I8_FAC1_FAI9_F1']"
    # 6.2 Acoustical Standards
    # 6.2.1
    section6_option_2a_yes = "//input[@originalid='V1_I1_S2_I5_O9']"
    section6_option_2a_no = "//input[@originalid='V1_I1_S2_I5_O10']"
    section6_option_2a_not = "//input[@originalid='V1_I1_S2_I5_O11']"
    # 6.2.1 上传
    section6_option_2a_updata_a = "//input[@originalid='V1_I1_S2_I5_S6_I7_S1_I8_FAC1_FAI9_F1']"
    section6_emiss_input_2a = "//input[@originalid='V1_I1_S2_I5_S12_I16_T3']"
    # 6.2.2
    section6_option_3a_yes = "//input[@originalid='V1_I1_S2_I5_S13_I20_O1']"
    section6_option_3a_no = "//input[@originalid='V1_I1_S2_I5_S13_I20_O2']"
    section6_option_3a_not = "//input[@originalid='V1_I1_S2_I5_S13_I20_O3']"
    # input
    section6_emiss_input_3a = "//input[@originalid='V1_I1_S2_I5_S13_I20_T4']"

    # Acoustic Product Levels  表格
    section6_levels_input_1a = "//input[@originalid='V1_I1_S2_I5_S14_I21_T1']"
    section6_levels_input_2a = "//input[@originalid='V1_I1_S2_I5_S14_I21_T2']"
    section6_levels_input_3a = "//input[@originalid='V1_I1_S2_I5_S14_I21_T3']"
    section6_levels_input_4a = "//input[@originalid='V1_I1_S2_I5_S14_I21_T4']"

    # Section 7 Environmentally Conscious Design
    # 7.1
    section7_option_1a_yes = "//input[@originalid='V1_I1_S2_I5_O2']"
    section7_option_1a_no = "//input[@originalid='V1_I1_S2_I5_O3']"
    section7_conscious_input_1a = "//textarea[@originalid='V1_I1_S2_I5_S4_I6_T1']"
    # 7.2 Prohibited Substances
    section7_checkbox_2a_1b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C1']"
    section7_checkbox_2a_2b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C2']"
    section7_checkbox_2a_3b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C3']"
    section7_checkbox_2a_4b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C4']"
    section7_checkbox_2a_5b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C5']"
    section7_checkbox_2a_6b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C6']"
    section7_checkbox_2a_7b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C7']"
    section7_checkbox_2a_8b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C8']"
    section7_checkbox_2a_9b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C9']"
    section7_checkbox_2a_10b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C10']"
    section7_checkbox_2a_11b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C11']"
    section7_checkbox_2a_12b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C12']"
    section7_checkbox_2a_13b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C13']"
    section7_checkbox_2a_14b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C14']"
    section7_checkbox_2a_15b = "//input[@originalid='V1_I1_S2_I5_S6_I9_C15']"
    # Provide the method used to verify absence of these substances.
    section7_select_2a = "//select[@originalid='V1_I1_S2_I5_S7_I10_D1']"
    section7_conscious_input_2a = "//div[@id='FormControl_V1_I1_S2_I5_RTC8_RTI11_RT1_newRichText']"
    # Systems?
    section7_option_2a_yes = "//input[@originalid='V1_I1_S2_I5_O9']"
    section7_option_2a_no = "//input[@originalid='V1_I1_S2_I5_O10']"
    # 7.2.1  section7_click_a
    section7_conscious_click_1a = "//a[@originalid='V1_I1_S2_I5_S11_I12_S1_I13_FAC1_FAI14_F1']"
    # 7.2.2  section7_click_a
    section7_conscious_click_2a = "//a[@originalid='V1_I1_S2_I5_S12_I16_FAC1_FAI17_F1']"
    # 7.3 Bill of Materials - Compliance Documents
    # 7.3.1
    section7_conscious_click_3a = "//a[@originalid='V1_I1_S2_I5_S14_I19_FAC1_FAI20_F1']"
    # 7.3.2
    section7_conscious_click_4a = "//a[@originalid='V1_I1_S2_I5_S17_I22_FAC1_FAI23_F1']"
    # 7.3.3. occurred?
    section7_option_3a_yes = "//input[@originalid='V1_I1_S2_I5_O19']"
    # input text
    section7_conscious_input_3a = "//textarea[@originalid='V1_I1_S2_I5_S21_I25_T1']"
    section7_option_3a_no = "//input[@originalid='V1_I1_S2_I5_O20']"
    # select
    section7_conscious_select_3a = "//select[@originalid='V1_I1_S2_I5_S22_I26_D1']"
    # 7.4 Plastic Standard
    section7_option_4a_yes = "//input[@originalid='V1_I1_S2_I5_O24']"
    section7_option_4a_no = "//input[@originalid='V1_I1_S2_I5_O25']"
    section7_option_4a_not = "//input[@originalid='V1_I1_S2_I5_O26']"
    section7_option_4a_to = "//input[@originalid='V1_I1_S2_I5_O27']"
    # input text
    section7_conscious_input_4a = "//textarea[@originalid='V1_I1_S2_I5_S28_I28_T1']"
    # 7.5 Polyvinyl Chloride Cables and Cords
    section7_option_5a_yes = "//input[@originalid='V1_I1_S2_I5_O30']"
    section7_option_5a_no = "//input[@originalid='V1_I1_S2_I5_O31']"

    section7_option_5a_yes_2a = "//input[@originalid='V1_I1_S2_I5_S32_I29_O1']"
    section7_option_5a_no_2a = "//input[@originalid='V1_I1_S2_I5_S32_I29_O2']"

    # input
    section7_cords_input_1a = "//textarea[@originalid='V1_I1_S2_I5_S33_I30_T1']"
    section7_cords_input_2a = "//textarea[@originalid='V1_I1_S2_I5_S34_I31_T1']"
    section7_cords_input_3a = "//textarea[@originalid='V1_I1_S2_I5_S34_I31_T2']"


    # 7.6 The ECO Declaration                           V1_I1_S2_I5_S43_I41_FAC1_FAI40_F1
    section7_conscious_click_6a = "//a[@originalid='V1_I1_S2_I5_S42_I39_FAC1_FAI40_F1']"
    # 选择文件
    select_file = "//input[@id='FileAttachmentUpload']"


if __name__ == "__main__":
    cla = element_position()
    #
    # print(.self.web.find_element(By.XPATH, cla.ele.section2_click293_a3).click())
































