<template>
	<view class="content">
		<u-form :model="form" ref="uForm">
			<u-form-item label="请假类型" label-width="150rpx">
				<u-radio-group v-model="radio4">
					<u-radio v-for="(item, index) in radioList4" :key="index" :name="item.name"
						:disabled="item.disabled" @change="radio4GroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="请假开始时间" prop='startTime' label-width="200rpx">
				<u-input v-model="form.startTime" />
			</u-form-item>
			<u-form-item label="请假结束时间" prop='endTime' label-width="200rpx">
				<u-input v-model="form.endTime" />
			</u-form-item>
			<u-form-item label="是否外出" label-width="200rpx">
				<u-radio-group v-model="radio">
					<u-radio v-for="(item, index) in radioList" :key="index" :name="item.name" :disabled="item.disabled"
						@change="radioGroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="是否出兰" label-width="200rpx">
				<u-radio-group v-model="radio2">
					<u-radio v-for="(item, index) in radioList2" :key="index" :name="item.name"
						:disabled="item.disabled" @change="radio2GroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="目的地" prop='destination' label-width="200rpx" v-show="radio2=='是'">
				<u-input v-model="form.destination" />
			</u-form-item>
			<u-form-item label="所乘交通工具" label-width="200rpx" v-show="radio2=='是'">
				<u-radio-group v-model="radio3">
					<u-radio v-for="(item, index) in radioList3" :key="index" :name="item.name"
						:disabled="item.disabled" @change="radio3GroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="车次/航班号/车牌号" prop='number' label-width="300rpx" v-show="radio2=='是'">
				<u-input v-model="form.number" />
			</u-form-item>
			</u-form-item>
			<u-form-item label="途径地" prop='onTheWay' label-width="200rpx" v-show="radio2=='是'">
				<u-input v-model="form.onTheWay" />
			</u-form-item>
			</u-form-item>
			<u-form-item label="乘车开始时间" prop='carStartTime' label-width="200rpx" v-show="radio2=='是'">
				<u-input v-model="form.carStartTime" />
			</u-form-item>
			</u-form-item>
			<u-form-item label="乘车结束时间" prop='carEndTime' label-width="200rpx" v-show="radio2=='是'">
				<u-input v-model="form.carEndTime" />
			</u-form-item>
			<u-form-item label="紧急联系人" prop='urgencyMan' label-width="200rpx">
				<u-input v-model="form.urgencyMan" />
			</u-form-item>
			<u-form-item label="与请假人关系" prop='relevant' label-width="200rpx">
				<u-input v-model="form.relevant" />
			</u-form-item>
			<u-form-item label="紧急联系人电话" prop='urgencyManPhoneNumber' label-width="220rpx">
				<u-input v-model="form.urgencyManPhoneNumber" />
			</u-form-item>
			<u-form-item label="本人QQ号码" prop='qq' label-width="200rpx">
				<u-input v-model="form.qq" />
			</u-form-item>
			<u-form-item label="本人电话号码" prop='phoneNumber' label-width="200rpx">
				<u-input v-model="form.phoneNumber" />
			</u-form-item>
			<u-form-item label="本人微信号码" prop='wx' label-width="200rpx">
				<u-input v-model="form.wx" />
			</u-form-item>
			<u-form-item label="请假事由" prop='happen' label-width="150rpx">
				<u-input v-model="form.happen" />
			</u-form-item>
			<u-form-item label="已阅读 《兰州大学本科生请销假管理办法》,外出已获得家长同意。" prop='check' label-width="550rpx">
				<u-switch slot="right" v-model="switchVal"></u-switch>
			</u-form-item>
			<u-button type="primary" shape="circle" :ripple="true" :custom-style="buttonStyle" @click='submit()'>点击提交申请
			</u-button>
		</u-form>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					startTime: '',
					endTime: '',
					destination: '',
					number: '',
					onTheWay: '',
					carStartTime: '',
					carEndTime: '',
					urgencyMan: '',
					relevant: '',
					urgencyManPhoneNumber: '',
					qq: '',
					phoneNumber: '',
					wx: '',
					happen: '',
				},
				rules: {
					startTime: [{
						required: true,
						message: '请输入请假开始时间',
						// 可以单个或者同时写两个触发验证方式 
						trigger: ['change', 'blur'],
					}],
					happen: [{
						min: 5,
						required: true,
						message: '请假事由不能少于5个字',
						trigger: ['change', 'blur'],
					}],
					endTime: [{
						required: true,
						message: '请输入请假结束时间',
						trigger: ['change', 'blur'],
					}],
					destination: [{
						required: true,
						message: '请输入目的地',
						trigger: ['change', 'blur'],
					}],
					number: [{
						required: true,
						message: '请输入车次/航班号/车牌号',
						trigger: ['change', 'blur'],
					}],
					onTheWay: [{
						required: true,
						message: '请输入途径地',
						trigger: ['change', 'blur'],
					}],
					carStartTime: [{
						required: true,
						message: '请输入乘车开始时间',
						trigger: ['change', 'blur'],
					}],
					carEndTime: [{
						required: true,
						message: '请输入乘车结束时间',
						trigger: ['change', 'blur'],
					}],
					urgencyMan: [{
						required: true,
						message: '请输入紧急联系人姓名',
						trigger: ['change', 'blur'],
					}],
					relevant: [{
						required: true,
						message: '请输入与请假人关系',
						trigger: ['change', 'blur'],
					}],
					urgencyManPhoneNumber: [{
						required: true,
						message: '请输入紧急联系人电话',
						trigger: ['change', 'blur'],
					}],
					qq: [{
						required: true,
						message: '请输入本人qq号',
						trigger: ['change', 'blur'],
					}],
					phoneNumber: [{
						required: true,
						message: '请输入本人电话号码',
						trigger: ['change', 'blur'],
					}],
					wx: [{
						required: true,
						message: '请输入本人微信号码',
						trigger: ['change', 'blur'],
					}],
				},
				buttonStyle: {
					marginRight: '40px', // 注意驼峰命名，并且值必须用引号包括，因为这是对象
				},
				radioList: [{
						name: '是',
						disabled: false
					},
					{
						name: '否',
						disabled: false
					}
				],
				radioList2: [{
						name: '是',
						disabled: false
					},
					{
						name: '否',
						disabled: false
					}
				],
				radioList3: [{
						name: '飞机',
						disabled: false
					},
					{
						name: '火车',
						disabled: false
					},
					{
						name: '其他',
						disabled: false
					}
				],
				radioList4: [{
					name: '实习',
					disabled: false
				}, {
					name: '返家',
					disabled: false
				}, {
					name: '旅游',
					disabled: false
				}, {
					name: '病假',
					disabled: false
				}, {
					name: '事假',
					disabled: false
				}, {
					name: '医学南校区',
					disabled: false
				}, {
					name: '其他',
					disabled: false
				}, {
					name: '毕业离校',
					disabled: false
				}, {
					name: '寒暑假离家',
					disabled: false
				}, ],
				radio: '',
				radio2: '',
				radio3: '',
				radio4: '',
				switchVal: false
			};
		},
		methods: {
			// 选中某个单选框时，由radio时触发
			radioGroupChange(e) {
				console.log(e);
			},
			radio2GroupChange(r) {
				console.log(r);
			},
			radio3GroupChange(t) {
				console.log(t);
			},
			radio4GroupChange(y) {
				console.log(y);
			},
			submit() {
				if (this.switchVal == true) {
					this.$refs.uForm.validate(valid => {
						if (valid) {
							console.log('验证通过');
							let that = this
							uni.request({
								url: '',
								method: 'POST',
								data: {
									startTime: that.startTime,
									endTime: that.endTime,
									destination: that.destination,
									number: that.number,
									onTheWay: that.onTheWay,
									carStartTime: that.carStartTime,
									carEndTime: that.carEndTime,
									urgencyMan: that.urgencyMan,
									relevant: that.relevant,
									urgencyManPhoneNumber: that.urgencyManPhoneNumber,
									qq: that.qq,
									phoneNumber: that.phoneNumber,
									wx: that.wx,
									happen: that.happen,
									goout: that.radio,
									outLan: that.radio2,
									vehicle: that.radio3,
									Type: that.radio4,
								},
								success: (res) => {
									if (res.data.status_code == 100) {
										uni.showToast({
											title: '提交成功'
										})
									} else {
										uni.showToast({
											title: '提交失败，请稍后重试'
										})
									}
								}
							})
						} else {
							console.log('验证失败');
							this.switchVal = false
						}
					});
				} else {
					console.log('请勾选同意');
				}
			}
		},
		onReady() {
			this.$refs.uForm.setRules(this.rules);
		},
	}
</script>

<style>
	.content {
		wight: 300rpx;
		margin-left: 100rpx;
		margin-right: 20rpx;
		display: flex;
		justify-content: center;
		align-content: center;
	}
</style>
