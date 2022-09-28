<template>
	<view class="content">
		<u-form :model="form" ref="uForm">
			<u-form-item label="请假类型" label-width="150rpx">
				<u-radio-group v-model="radio4">
					<u-radio v-for="(item, index) in radioList4" :key="index" :name="item.value"
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
					<u-radio v-for="(item, index) in radioList" :key="index" :name="item.value" :disabled="item.disabled"
						@change="radioGroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="是否出兰" label-width="200rpx">
				<u-radio-group v-model="radio2">
					<u-radio v-for="(item, index) in radioList2" :key="index" :name="item.value"
						:disabled="item.disabled" @change="radio2GroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="目的地" prop='destination' label-width="200rpx" v-show="radio2=='1'">
				<u-input v-model="form.destination" />
			</u-form-item>
			<u-form-item label="所乘交通工具" label-width="200rpx" v-show="radio2=='1'">
				<u-radio-group v-model="radio3">
					<u-radio v-for="(item, index) in radioList3" :key="index" :name="item.value"
						:disabled="item.disabled" @change="radio3GroupChange">
						{{ item.name }}
					</u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="车次/航班号/车牌号" prop='number' label-width="300rpx" v-show="radio=='1'">
				<u-input v-model="form.number" />
			</u-form-item>
			</u-form-item>
			<u-form-item label="途径地" prop='onTheWay' label-width="200rpx" v-show="radio=='1'">
				<u-input v-model="form.onTheWay" />
			</u-form-item>
			</u-form-item>
			<u-form-item label="乘车开始时间" prop='carStartTime' label-width="200rpx" v-show="radio=='1'">
				<u-input v-model="form.carStartTime" />
			</u-form-item>
			</u-form-item>
			<u-form-item label="乘车结束时间" prop='carEndTime' label-width="200rpx" v-show="radio=='1'">
				<u-input v-model="form.carEndTime" />
			</u-form-item>
			<u-form-item label="紧急联系人" prop='urgencyMan' label-width="200rpx" v-show="radio=='1'">
				<u-input v-model="form.urgencyMan" />
			</u-form-item>
			<u-form-item label="与请假人关系" prop='relevant' label-width="200rpx" v-show="radio=='1'">
				<u-input v-model="form.relevant" />
			</u-form-item>
			<u-form-item label="紧急联系人电话" prop='urgencyManPhoneNumber' label-width="220rpx" v-show="radio=='1'">
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
				
				buttonStyle: {
					marginRight: '40px', // 注意驼峰命名，并且值必须用引号包括，因为这是对象
				},
				radioList: [{
						name: '是',
						disabled: false,
						value:'1'
					},
					{
						name: '否',
						disabled: false,
						value:'0'
					}
				],
				radioList2: [{
						name: '是',
						disabled: false,
						value:'1'
					},
					{
						name: '否',
						disabled: false,
						value:'0'
					}
				],
				radioList3: [{
						name: '飞机',
						disabled: false,
						value:'0'
					},
					{
						name: '火车',
						disabled: false,
						value:'1'
					},
					{
						name: '其他',
						disabled: false,
						value:'2'
					}
				],
				radioList4: [{
					name: '实习',
					disabled: false,
					value:'01'
				}, {
					name: '返家',
					disabled: false,
					value:'03'
				}, {
					name: '旅游',
					disabled: false,
					value:'05'
				}, {
					name: '病假',
					disabled: false,
					value:'06'
				}, {
					name: '事假',
					disabled: false,
					value:'07'
				}, {
					name: '医学南校区',
					disabled: false,
					value:'08'
				}, {
					name: '其他',
					disabled: false,
					value:'09'
				}, {
					name: '毕业离校',
					disabled: false,
					value:'15'
				}, {
					name: '寒暑假离家',
					disabled: false,
					value:'20'
				}, ],
				radio: '',
				radio2: '',
				radio3: '',
				radio4: '',
				switchVal: false
			};
		},
		onLoad(res) {
			let that = this;
			setInterval(function(){
				uni.setStorageSync('startTime',that.startTime)
				uni.setStorageSync('endTime',that.endTime)
				uni.setStorageSync('destination',that.destination)
				uni.setStorageSync('number',that.number)
				uni.setStorageSync('onTheWay',that.onTheWay)
				uni.setStorageSync('carStarTime',that.carStartTime)
				uni.setStorageSync('carEndTime',that.carEndTime)
				uni.setStorageSync('urgencyMan',that.urgencyMan)
				uni.setStorageSync('relevant',that.relevant)
				uni.setStorageSync('urgencyManPhoneNumber',that.urgencyManPhoneNumber)
				uni.setStorageSync('qq',that.qq)
				uni.setStorageSync('phoneNumber',that.phoneNumber)
				uni.setStorageSync('wx',that.wx)
				uni.setStorageSync('happen',that.happen)
				uni.setStorageSync('goout',that.radio)
				uni.setStorageSync('outLan',that.radio2)
				uni.setStorageSync('vehicle',that.radio3)
				uni.setStorageSync('Type',that.radio4)
			},2000)
		},
		onShow() {
			this.startTime = uni.getStorageSync('startTime')
			this.endTime = uni.getStorageSync('endTime')
			this.destination = uni.getStorageSync('destination')
			this.number = uni.getStorageSync('number')
			this.onTheWay = uni.getStorageSync('onTheWay')
			this.carStartTime = uni.getStorageSync('carStartTime')
			this.carEndTime = uni.getStorageSync('carEndTime')
			this.urgencyMan = uni.getStorageSync('urgencyMan')
			this.urgencyManPhoneNumber = uni.getStorageSync('urgencyManPhoneNumber')
			this.qq = uni.getStorageSync('qq')
			this.phoneNumber = uni.getStorageSync('phoneNumber')
			this.wx = uni.getStorageSync('wx')
			this.happen = uni.getStorageSync('happen')
			this.radio = uni.getStorageSync('goout')
			this.radio2 = uni.getStorageSync('outLan')
			this.radio3 = uni.getStorageSync('vehicle')
			this.radio4 = uni.getStorageSync('Type')
		},
		methods: {
			// 选中某个单选框时，由radio时触发
			radioGroupChange(e) {
				this.radio = e
			},
			radio2GroupChange(r) {
				this.radio2 = r			},
			radio3GroupChange(t) {
				this.radio3 = t
			},
			radio4GroupChange(y) {
				this.radio4 = y
				console.log(this.radio4)
				},			
			submit() {
				console.log(this.radio4)
				if (this.switchVal == true) {
					this.$refs.uForm.validate(valid => {
						if (valid) {
							console.log('验证通过');
							
							uni.request({
								url: 'http://127.0.0.1:8000/tableSubmit/dayoffSubmit',
								method: 'GET',
								data: {
									startTime: this.form.startTime,
									endTime: this.form.endTime,
									destination: this.form.destination,
									number: this.form.number,
									onTheWay: this.form.onTheWay,
									carStartTime: this.form.carStartTime,
									carEndTime: this.form.carEndTime,
									urgencyMan: this.form.urgencyMan,
									relevant: this.form.relevant,
									urgencyManPhoneNumber: this.form.urgencyManPhoneNumber,
									qq: this.form.qq,
									phoneNumber: this.form.phoneNumber,
									wx: this.form.wx,
									happen: this.form.happen,
									goout: this.radio,
									outLan: this.radio2,
									vehicle: this.radio3,
									Type: this.radio4,
								},
								success: (res) => {
									if (res.data.status_code == 100) {
										uni.showToast({
											title: this.form.wx
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
